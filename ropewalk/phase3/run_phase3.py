import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import csv
import json
import multiprocessing as mp
import sys
import time
from pathlib import Path
import numpy as np
import scipy
import emcee
import matplotlib
import psutil

PHASE3_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PHASE3_DIR, ".."))
if PHASE3_DIR not in sys.path:
    sys.path.insert(0, PHASE3_DIR)
if os.path.join(ROOT_DIR, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))
if os.path.join(ROOT_DIR, "head_to_head") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "head_to_head"))

from phase3_wrappers import (
    BASE_SEED,
    set_below_normal_priority,
    run_single_cosmo_mcmc_task,
    assemble_cosmo_universe_result,
    run_single_galaxy_universe,
    run_single_regional_universe,
)

N_CORES = 12


def log_activity(msg: str):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S")
    line = f"{ts} - {msg}\n"
    log_path = os.path.join(PHASE3_DIR, "ACTIVITY_LOG_PHASE3.md")
    with open(log_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(line.strip())
    sys.stdout.flush()


def load_mock_manifest() -> list[dict]:
    manifest_path = os.path.join(ROOT_DIR, "MOCKS_FOR_ARGON", "MOCK_MANIFEST.csv")
    rows = []
    with open(manifest_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, r in enumerate(reader):
            rows.append({
                "index": idx,
                "universe_id": r["universe_id"].strip(),
                "family": r["family"].strip(),
                "round": int(r["round"].strip()),
                "u_dir": os.path.join(ROOT_DIR, "MOCKS_FOR_ARGON", r["universe_id"].strip()),
            })
    return rows


def build_cosmo_tasks_for_universe(u_row: dict) -> list[dict]:
    u_id = u_row["universe_id"]
    u_dir = u_row["u_dir"]
    u_idx = u_row["index"]
    ref_path = os.path.join(u_dir, "REFERENCES.json")
    with open(ref_path, "r", encoding="utf-8") as f:
        refs = json.load(f)
    bbn_prior = (
        float(refs["BBN_100omega_b_prior"]["value"]),
        float(refs["BBN_100omega_b_prior"]["sigma"]),
    )

    tasks = []
    slot = 1
    for reading in ["B", "A"]:
        for sn_name in ["Pantheon+", "DES-Dovekie"]:
            for model_kind in ["LAW1", "CPL", "T2A_CPL", "LCDM"]:
                cmb_mode = "conditional_2x2" if model_kind == "T2A_CPL" else "full_3x3"
                bbn_use = bbn_prior if model_kind == "T2A_CPL" else None
                run_id = f"{u_id}__R{reading}__{model_kind}__{sn_name}"
                seed = BASE_SEED + 1000 * (u_idx + 1) + slot
                slot += 1
                tasks.append({
                    "universe_id": u_id,
                    "u_dir": u_dir,
                    "round": u_row["round"],
                    "run_id": run_id,
                    "model_kind": model_kind,
                    "sn_name": sn_name,
                    "reading": reading,
                    "cmb_mode": cmb_mode,
                    "bbn_prior": bbn_use,
                    "seed": seed,
                })
    # Sort so slower LAW1 chains launch first in worker pool
    model_prio = {"LAW1": 0, "CPL": 1, "T2A_CPL": 2, "LCDM": 3}
    tasks.sort(key=lambda t: (model_prio[t["model_kind"]], t["reading"], t["sn_name"]))
    return tasks


def save_universe_log(u_res: dict):
    logs_dir = os.path.join(PHASE3_DIR, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    out_path = os.path.join(logs_dir, f"{u_res['universe_id']}.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(u_res, f, indent=2)


def load_existing_universe_log(u_id: str) -> dict | None:
    out_path = os.path.join(PHASE3_DIR, "logs", f"{u_id}.json")
    if os.path.exists(out_path):
        with open(out_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def main():
    set_below_normal_priority()
    os.makedirs(os.path.join(PHASE3_DIR, "logs"), exist_ok=True)

    manifest = load_mock_manifest()
    by_round = {}
    for row in manifest:
        by_round.setdefault(row["round"], []).append(row)

    total_start = time.perf_counter()
    all_results = {}
    round_runtimes = {}

    with mp.Pool(processes=N_CORES, initializer=set_below_normal_priority) as pool:
        # Step 1: First universe of each family in Round 1 to measure & log runtime and projected total
        r1_rows = by_round[1]
        first_galaxy = next(r for r in r1_rows if r["family"] == "GALAXY")
        first_cosmo = next(r for r in r1_rows if r["family"] == "COSMO")
        first_regional = next(r for r in r1_rows if r["family"] == "REGIONAL")

        log_activity(
            f"Starting Round 1 first-universe benchmark across families: "
            f"{first_galaxy['universe_id']} (GALAXY), {first_cosmo['universe_id']} (COSMO), {first_regional['universe_id']} (REGIONAL)."
        )

        # 1a. First GALAXY universe
        t0 = time.perf_counter()
        g_task = {
            **first_galaxy,
            "seed": BASE_SEED + 2000 * (first_galaxy["index"] + 1),
        }
        res_g1 = run_single_galaxy_universe(g_task)
        t_gal_1 = time.perf_counter() - t0
        res_g1["elapsed_sec"] = round(t_gal_1, 3)
        save_universe_log(res_g1)
        all_results[first_galaxy["universe_id"]] = res_g1
        log_activity(
            f"Completed first GALAXY universe {first_galaxy['universe_id']} in {t_gal_1:.2f}s "
            f"(projected 15 GALAXY universes serial = {15.0 * t_gal_1:.1f}s)."
        )

        # 1b. First REGIONAL universe
        t0 = time.perf_counter()
        res_r1 = run_single_regional_universe(first_regional)
        t_reg_1 = time.perf_counter() - t0
        res_r1["elapsed_sec"] = round(t_reg_1, 3)
        save_universe_log(res_r1)
        all_results[first_regional["universe_id"]] = res_r1
        log_activity(
            f"Completed first REGIONAL universe {first_regional['universe_id']} in {t_reg_1:.2f}s "
            f"(projected 15 REGIONAL universes serial = {15.0 * t_reg_1:.1f}s)."
        )

        # 1c. First COSMO universe (16 MCMC chains across 12 workers)
        t0 = time.perf_counter()
        c1_tasks = build_cosmo_tasks_for_universe(first_cosmo)
        c1_chains = list(pool.imap_unordered(run_single_cosmo_mcmc_task, c1_tasks))
        t_cos_1 = time.perf_counter() - t0
        res_c1 = assemble_cosmo_universe_result(
            first_cosmo["universe_id"], first_cosmo["round"], first_cosmo["u_dir"], c1_chains, t_cos_1
        )
        save_universe_log(res_c1)
        all_results[first_cosmo["universe_id"]] = res_c1

        proj_total_sec = 15.0 * t_cos_1 + 5.0 * t_gal_1 + 5.0 * t_reg_1
        proj_serial_universe_sum_sec = 15.0 * (t_cos_1 + t_gal_1 + t_reg_1)
        log_activity(
            f"Completed first COSMO universe {first_cosmo['universe_id']} in {t_cos_1:.2f}s. "
            f"Projected 45-universe total wall-clock runtime = {proj_total_sec:.1f}s ({proj_total_sec / 60.0:.2f} min; "
            f"sum of 15x first-universe times = {proj_serial_universe_sum_sec:.1f}s = {proj_serial_universe_sum_sec / 60.0:.2f} min) "
            f"<< 24h limit (86,400s). Proceeding to complete all 5 rounds."
        )

        runtime_projection = {
            "first_galaxy_universe": first_galaxy["universe_id"],
            "first_galaxy_sec": round(t_gal_1, 3),
            "first_regional_universe": first_regional["universe_id"],
            "first_regional_sec": round(t_reg_1, 3),
            "first_cosmo_universe": first_cosmo["universe_id"],
            "first_cosmo_sec": round(t_cos_1, 3),
            "projected_total_parallel_sec": round(proj_total_sec, 2),
            "projected_total_parallel_min": round(proj_total_sec / 60.0, 2),
            "projected_total_15x_sum_sec": round(proj_serial_universe_sum_sec, 2),
            "projected_total_15x_sum_min": round(proj_serial_universe_sum_sec / 60.0, 2),
            "limit_sec": 86400,
            "fits_within_24h": bool(proj_serial_universe_sum_sec < 86400.0),
        }
        with open(os.path.join(PHASE3_DIR, "logs", "runtime_projection.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(runtime_projection, f, indent=2)

        # Step 2: Process remaining universes of Round 1, then Rounds 2..5 in order
        for r_num in sorted(by_round.keys()):
            t_round_start = time.perf_counter()
            r_rows = by_round[r_num]
            pending_rows = [r for r in r_rows if r["universe_id"] not in all_results]

            if pending_rows:
                log_activity(
                    f"Running Round {r_num} ({len(pending_rows)} pending universes: "
                    f"{', '.join(r['universe_id'] for r in pending_rows)})..."
                )

                # Separate by family inside the round
                gal_rows = [r for r in pending_rows if r["family"] == "GALAXY"]
                reg_rows = [r for r in pending_rows if r["family"] == "REGIONAL"]
                cos_rows = [r for r in pending_rows if r["family"] == "COSMO"]

                # Run GALAXY universes in parallel
                if gal_rows:
                    gal_tasks = [
                        {**r, "seed": BASE_SEED + 2000 * (r["index"] + 1)}
                        for r in gal_rows
                    ]
                    for g_res in pool.imap_unordered(run_single_galaxy_universe, gal_tasks):
                        save_universe_log(g_res)
                        all_results[g_res["universe_id"]] = g_res
                        log_activity(
                            f"Completed {g_res['universe_id']} (GALAXY, Round {r_num}) in {g_res['elapsed_sec']:.2f}s."
                        )

                # Run REGIONAL universes in parallel
                if reg_rows:
                    for reg_res in pool.imap_unordered(run_single_regional_universe, reg_rows):
                        save_universe_log(reg_res)
                        all_results[reg_res["universe_id"]] = reg_res
                        log_activity(
                            f"Completed {reg_res['universe_id']} (REGIONAL, Round {r_num}) in {reg_res['elapsed_sec']:.2f}s."
                        )

                # Run COSMO universes in this round across the 12-worker pool
                if cos_rows:
                    t_cos_batch = time.perf_counter()
                    batch_tasks = []
                    for cr in cos_rows:
                        batch_tasks.extend(build_cosmo_tasks_for_universe(cr))
                    model_prio = {"LAW1": 0, "CPL": 1, "T2A_CPL": 2, "LCDM": 3}
                    batch_tasks.sort(key=lambda t: (model_prio[t["model_kind"]], t["reading"], t["sn_name"], t["universe_id"]))

                    chains_by_u = {cr["universe_id"]: [] for cr in cos_rows}
                    u_start_map = {cr["universe_id"]: t_cos_batch for cr in cos_rows}
                    u_row_map = {cr["universe_id"]: cr for cr in cos_rows}

                    for ch_res in pool.imap_unordered(run_single_cosmo_mcmc_task, batch_tasks):
                        uid = ch_res["universe_id"]
                        chains_by_u[uid].append(ch_res)
                        if len(chains_by_u[uid]) == 16:
                            u_elapsed = time.perf_counter() - u_start_map[uid]
                            cr = u_row_map[uid]
                            u_assembled = assemble_cosmo_universe_result(
                                uid, cr["round"], cr["u_dir"], chains_by_u[uid], u_elapsed
                            )
                            save_universe_log(u_assembled)
                            all_results[uid] = u_assembled
                            log_activity(
                                f"Completed {uid} (COSMO, Round {r_num}) in {u_elapsed:.2f}s wall-clock "
                                f"(sum of 16 chain CPU times = {sum(c['elapsed_sec'] for c in chains_by_u[uid]):.1f}s)."
                            )

            round_sec = time.perf_counter() - t_round_start
            if r_num == 1:
                round_sec += t_gal_1 + t_reg_1 + t_cos_1
            round_runtimes[f"Round_{r_num}"] = round(round_sec, 3)
            log_activity(f"Finished Round {r_num} (all 9 universes complete; Round {r_num} elapsed = {round_sec:.2f}s).")

    total_wall_sec = time.perf_counter() - total_start
    ordered_universes = [all_results[row["universe_id"]] for row in manifest]

    master_out = {
        "label": "Phase 3 injection tests: supplementary, not pre-registered in Stage 1",
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S-04:00"),
        "total_wall_clock_sec": round(total_wall_sec, 3),
        "total_universes_analyzed": len(ordered_universes),
        "rounds_completed": [1, 2, 3, 4, 5],
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "emcee": emcee.__version__,
            "matplotlib": matplotlib.__version__,
            "psutil": psutil.__version__,
            "n_cores": N_CORES,
            "base_seed": BASE_SEED,
        },
        "runtime_projection_after_first_per_family": runtime_projection,
        "round_runtimes_sec": round_runtimes,
        "per_universe_runtimes_sec": {
            u["universe_id"]: {
                "family": u["family"],
                "round": u["round"],
                "elapsed_sec": u["elapsed_sec"],
            }
            for u in ordered_universes
        },
        "universes": {u["universe_id"]: u for u in ordered_universes},
        "universes_in_manifest_order": ordered_universes,
    }

    results_path = os.path.join(PHASE3_DIR, "results.json")
    with open(results_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(master_out, f, indent=2)
    log_activity(f"Saved master Phase 3 results to {results_path} (total wall-clock = {total_wall_sec:.2f}s).")


if __name__ == "__main__":
    main()
