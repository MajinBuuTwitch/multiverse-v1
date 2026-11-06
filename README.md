# MULTIVERSE v1: A Pre-Registered Falsification of a Speculative Multiverse Model

**Paper:** `paper/MULTIVERSE_V1_PAPER.pdf` · **DOI:** [10.5281/zenodo.23868218](https://doi.org/10.5281/zenodo.23868218) · **Video:** https://youtu.be/KZ_8tOKs3xE

This repository is the complete public record behind the MULTIVERSE documentary (WickedAI, 2026). It tests version 1 of the Mandarano Model, a speculative model written for the documentary, against public cosmological and galactic data under rules that were frozen before any data were downloaded and anchored in the Bitcoin blockchain before any test ran.

**Result: version 1 is falsified.** Its galaxy rotation-curve pillar (T5-A) fails decisively in two independent pipelines, and blind injection tests confirm the pipeline gets that test right in both directions. Its one-in-nineteen predictions miss by 3.7 to 3.9σ, and its leak ratio misses by 3.2 to 3.7σ. Its dark-energy curve is neither confirmed nor ruled out. Nothing in this repository is claimed as new physics.

## What is here

Each pipeline's workspace is mirrored with its original folder layout, so every manifest verifies from inside its own folder.

| Folder | Contents |
|:--|:--|
| `paper/` | The paper (Markdown source and PDF) |
| `ropewalk/` | The primary pipeline (Gemini 4 "Argon"): rulebook (`PREREG_v4`), data manifest, Stage 2 code and frozen results (`RESULTS_v1` to `v5`), the Bayesian head-to-head, the Phase 3 analysis, logs, and every manifest with its timestamp proof |
| `ropewalk/archive/` | Earlier file versions that the superseded manifests (`RESULTS_v1` to `v4`, `PREREG_v1` to `v3`) list, with `PATH_MAP.txt` |
| `blind_rebuild/` | The blind independent rebuild (Claude Opus 5.5): code, frozen results (`REBUILD_RESULTS_v1`), deviations, logs, the Phase 3 mock generator, sealed truths and answer key |
| `multiverse_review/` | The independent Phase 3 re-score (separate Gemini session): its six inputs, report and script |
| `planner/` | The planning session's Phase 3 scoring, addenda and stamps, and upgraded timestamp proofs for manifests held here |
| `v2_design/` | Version 2's design record as it stands: the append-only design log with a proof for every entry, the math log, the charter, the fenced-data list, both dark-energy freezes (DE-F1 and its replacement DE-F2), the frozen v2 specification (Stage 2.4, SPEC_FREEZE_v1), and notes for the v2 paper. Version 2 has not been tested; nothing in it is a result. |

Third-party datasets and arXiv source files are not redistributed; `download_data.py` fetches them and checks every file against its manifest. The Phase 3 mock folders omit 60 unmodified copies of third-party covariance files; `restore_mock_covariances.py` copies them back after the download.

## How to verify it yourself

1. **Fingerprints.** From inside the workspace folder (`ropewalk/`, `blind_rebuild/`, ...), run `sha256sum -c <manifest>.sha256`. Four known cases need care: append-only logs are checked over the frozen prefix length the manifest records (`head -c N file | sha256sum`); some manifest lines carry trailing `#` comments to remove first; superseded manifests list earlier file versions kept in `archive/` (see `PATH_MAP.txt`); and two results manifests list plan proofs by their pre-upgrade fingerprint, kept as `.ots.bak` beside the upgraded `.ots`.
2. **Timestamps.** Install the OpenTimestamps client (`pip install opentimestamps-client`) and run `ots verify <manifest>.sha256.ots`. It reports the Bitcoin block the manifest existed by.
3. **Order.** Check that the rulebook was stamped before the data manifest, both before any results, and Phase 3's sealed truths before its analysis plan and both before its results. Appendix A of the paper lists every block.
4. **Data.** Third-party datasets are not redistributed here. Run `python download_data.py` from the repository root: it fetches everything the pipelines used (with TLS certificate checks on) into the folders the manifests expect, never overwrites a file in the repository, and prints PASS or FAIL for every line of `ropewalk/DATA_MANIFEST.sha256`, the cluster e-prints in `ropewalk/RESULTS_v5.sha256`, and the rebuild's `DATA_MANIFEST_REBUILD*.sha256`. Then run `python restore_mock_covariances.py`. The downloaded data is git-ignored. `ropewalk/scripts/get_data.py` is kept unchanged as part of the frozen record; don't run it inside the repository: it rewrites two frozen files (`data/MANIFEST.csv`, `data/registered_priors.json`) and turns off certificate checks.
5. **Rerun.** Each pipeline folder has a README with its pinned environment and the exact commands used.

An independent audit of this repository by the planning session, run on a fresh clone, is in planner/PLANNER_REPO_AUDIT.txt.

### Append-only logs

These logs kept growing after they were frozen, so each manifest fingerprints only the first N bytes. From the folder that holds the manifest, check with `head -c N FILE | sha256sum` and compare with the manifest line.

| Log | Manifest that freezes it | Frozen prefix (bytes) |
|:--|:--|--:|
| `ropewalk/ACTIVITY_LOG.md` | `ropewalk/PREREG_v2.sha256` | 10,154 |
| `ropewalk/ACTIVITY_LOG.md` | `ropewalk/archive/PREREG_v3_prelim.sha256` | 15,814 |
| `ropewalk/ACTIVITY_LOG.md` | `ropewalk/PREREG_v3.sha256` | 17,891 |
| `ropewalk/ACTIVITY_LOG.md` | `ropewalk/PREREG_v4.sha256` | 23,542 |
| `ropewalk/ACTIVITY_LOG.md` | `ropewalk/RESULTS_v4.sha256` | 38,017 |
| `blind_rebuild/ACTIVITY_LOG_REBUILD.md` | `blind_rebuild/REBUILD_RESULTS_v1.sha256` | 16,271 |
| `blind_rebuild/phase3/SEALED/GENERATION_LOG.md` | `blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256` (paths relative to `blind_rebuild/phase3/`) | 28,402 |
| `v2_design/MULTIVERSE_V2_PAPER_NOTES.txt` | `v2_design/MULTIVERSE_V2_DESIGN_LOG_e36.sha256` | 8,788 |
| `v2_design/MULTIVERSE_V2_PAPER_NOTES.txt` | `v2_design/MULTIVERSE_V2_DESIGN_LOG_e41.sha256` | 25,484 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG.txt` | `v2_design/MULTIVERSE_V2_DE_FREEZE_F1.sha256` | 55,106 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG.txt` | `v2_design/MULTIVERSE_V2_DE_FREEZE_F2.sha256` | 84,597 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG.txt` | `v2_design/MULTIVERSE_V2_DESIGN_LOG_eN.sha256`, one per entry: e2 3,562 · e3 7,220 · e4 8,850 · e5 11,106 · e6 13,272 · e7 15,265 · e8 15,843 · e9 18,856 · e10 22,392 · e11 25,664 · e12 26,684 · e13 28,082 · e14 29,781 · e15 31,001 · e16 33,068 · e17 34,894 · e18 36,498 · e19 38,091 · e20 39,869 · e21 42,226 · e22 45,531 · e23 48,106 · e24 49,513 · e25 51,908 · e26 53,001 · e27 54,030 · e28 55,106 · e29 57,365 · e30 58,751 · e31 60,416 · e32 61,421 · e33 63,923 · e34 64,610 · e35 65,498 · e36 66,366 · e37 68,337 · e37b 68,686 · e38 70,982 · e39 84,597 · e40 90,907 · e41 100,670 · e42 107,542 · e43 113,641 · e44 122,088 · e45 133,559 · e46 140,809 · e47 163,041 (full length) | per entry |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG.txt` and `v2_design/MULTIVERSE_V2_SPEC.txt` | `v2_design/MULTIVERSE_V2_SPEC_FREEZE_v1.sha256` | 163,041 and 92,575 (full) |

`RESULTS_v5.sha256` fingerprints `ropewalk/ACTIVITY_LOG.md` at its full current length. `MULTIVERSE_V2_DESIGN_LOG_e47.sha256` and `MULTIVERSE_V2_SPEC_FREEZE_v1.sha256` fingerprint `MULTIVERSE_V2_DESIGN_LOG.txt` at its full current length (163,041 bytes), and the freeze also fingerprints the frozen v2 specification `MULTIVERSE_V2_SPEC.txt` in full (92,575 bytes). `MULTIVERSE_V2_DESIGN_LOG_e41.sha256` still fingerprints `MULTIVERSE_V2_PAPER_NOTES.txt` at its full current length (25,484 bytes). `MULTIVERSE_V2_DE_FREEZE_F2.sha256` also fingerprints the charter and the fenced-data list in full.

## Honest limits

The paper's Limitations section is the full list. In short: several datasets were public before the rules were written, so only the held-out galaxy, cluster and regional tests are genuinely blind; one sound-horizon convention has two readings and both are reported; the cluster test was under-powered by design; and the blind injection tests validated the decisive galaxy pillar but did not meet their overall locked validation criterion. Every miss is reported, not patched.

## Who did what

- **Gregory Mandarano (WickedAI):** the model, the rules, every decision, the documentary.
- **Claude Opus 5.5 (Anthropic, `claude-opus-5-5`):** planning, rule drafting, review, Phase 3 scoring, paper drafting.
- **Claude Opus 5.5 (Anthropic, claude-opus-5-5) at high effort:** the blind independent rebuild (its first half hour in Google Antigravity through Antigravity's third-party model access, then Claude Code on the same folder and instructions, per the author; the rebuild's logs record the Claude Code stage) and the Phase 3 mock generator.
- **Gemini 4 "Argon" (Google)**, in Google Antigravity, instructed to run at the High thinking level (the logs record no finer version string): the primary pipeline, the head-to-head and the Phase 3 analysis.
- **Gemini (Google), separate session:** the independent Phase 3 re-score. **Grok (xAI):** external review.

## Contact

Questions about the record: GregoryMandarano@gmail.com.

## Licence

Code: MIT (`LICENSE`). Paper, text and figures: CC BY 4.0 (`LICENSE-DOCS`). Third-party data keep their own licences and are fetched from their sources.

## Cite

See `CITATION.cff`, or cite the Zenodo DOI above.
