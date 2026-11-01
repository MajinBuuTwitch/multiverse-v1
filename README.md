# MULTIVERSE v1: A Pre-Registered Falsification of a Speculative Multiverse Model

**Paper:** `paper/MULTIVERSE_V1_PAPER.pdf` · **DOI:** [ZENODO DOI] · **Video:** [YOUTUBE LINK]

This repository is the complete public record behind the MULTIVERSE documentary (WickedAI, 2026). It tests version 1 of the Mandarano Model, a speculative model written for the documentary, against public cosmological and galactic data under rules that were frozen and anchored in the Bitcoin blockchain before any data were downloaded.

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
| `v2_design/` | Version 2's design record as it stands: the append-only design log with a proof for every entry, the math log, the charter, the fenced-data list, the dark-energy freeze, and notes for the v2 paper. Version 2 has not been tested; nothing in it is a result. |

Third-party datasets and arXiv source files are not redistributed; `ropewalk/scripts/get_data.py` fetches them and `DATA_MANIFEST.sha256` checks them. The Phase 3 mock folders omit 60 unmodified copies of third-party covariance files; `restore_mock_covariances.py` copies them back after the download.

## How to verify it yourself

1. **Fingerprints.** From inside the workspace folder (`ropewalk/`, `blind_rebuild/`, ...), run `sha256sum -c <manifest>.sha256`. Four known cases need care: append-only logs are checked over the frozen prefix length the manifest records (`head -c N file | sha256sum`); some manifest lines carry trailing `#` comments to remove first; superseded manifests list earlier file versions kept in `archive/` (see `PATH_MAP.txt`); and two results manifests list plan proofs by their pre-upgrade fingerprint, kept as `.ots.bak` beside the upgraded `.ots`.
2. **Timestamps.** Install the OpenTimestamps client (`pip install opentimestamps-client`) and run `ots verify <manifest>.sha256.ots`. It reports the Bitcoin block the manifest existed by.
3. **Order.** Check that the rulebook was stamped before the data manifest, both before any results, and Phase 3's sealed truths before its analysis plan and both before its results. Appendix A of the paper lists every block.
4. **Data.** Third-party datasets are not redistributed here. Run `python ropewalk/scripts/get_data.py` from a copy of `ropewalk/` (it rewrites the frozen `data/MANIFEST.csv` and `data/registered_priors.json`), then check the files against `ropewalk/DATA_MANIFEST.sha256` and run `python restore_mock_covariances.py --data <that copy>/data`.
5. **Rerun.** Each pipeline folder has a README with its pinned environment and the exact commands used.

## Honest limits

The paper's Limitations section is the full list. In short: several datasets were public before the rules were written, so only the held-out galaxy, cluster and regional tests are genuinely blind; one sound-horizon convention has two readings and both are reported; the cluster test was under-powered by design; and the blind injection tests validated the decisive galaxy pillar but did not meet their overall locked validation criterion. Every miss is reported, not patched.

## Who did what

- **Gregory Mandarano (WickedAI):** the model, the rules, every decision, the documentary.
- **Claude Opus 5.5 (Anthropic, `claude-opus-5-5`):** planning, rule drafting, review, Phase 3 scoring, paper drafting.
- **Claude Code (Anthropic) [VERSION FROM LOGS]:** the blind independent rebuild and the Phase 3 mock generator.
- **Gemini 4 "Argon" (Google) [VERSION FROM LOGS]:** the primary pipeline, the head-to-head and the Phase 3 analysis.
- **Gemini (Google), separate session:** the independent Phase 3 re-score. **Grok (xAI):** external review.

## Contact

Questions about the record: GregoryMandarano@gmail.com.

## Licence

Code: MIT (`LICENSE`). Paper, text and figures: CC BY 4.0 (`LICENSE-DOCS`). Third-party data keep their own licences and are fetched from their sources.

## Cite

See `CITATION.cff`, or cite the Zenodo DOI above.
