# Standing Project Rules & Guardrails (Ropewalk Multiverse Project)

These rules govern every turn, command, and file operation in this workspace (`D:\Argon_Code\Ropewalk`). No exceptions.

## 1. Execution Pacing & State Persistence
- **Work in numbered parts.** Stop completely at the end of each numbered part and wait for the user to type `CONTINUE`.
- **Save every result to disk** inside this workspace at the end of every part.
- **Maintain `ACTIVITY_LOG.md`:** Append one line for every command executed and every file created or modified, prefixed with the local ISO-8601 timestamp (`YYYY-MM-DDTHH:MM:SS`).

## 2. Scientific Integrity & Pre-Registration
- **No parameter tuning and no threshold changes** after seeing any test data.
- **Report failures as plainly as passes.** Never soften, excuse, or re-frame a failed test criterion.
- **Flag every assumption explicitly** in all theoretical and numerical work.
- **Classify every equation:** Mark every equation explicitly as either `[Established]` (standard physics/cosmology) or `[Model Ansatz]` (specific to the speculative model or its mapping).
- **`MULTIVERSE_TESTS_v1.md` is locked and read-only.** Its pass/fail criteria are fixed in advance and may never be altered.

## 3. Strict Workspace & File Isolation
- **Stay strictly inside `D:\Argon_Code\Ropewalk`.** Never read, write, modify, or execute anything that touches the C: drive or any folder outside `D:\Argon_Code\Ropewalk` (except standard OS/PowerShell binaries needed to execute commands, and downloading public datasets from the internet directly into `D:\Argon_Code\Ropewalk`).
- **Local Python virtual environment only:** All Python packages must be installed inside a local virtual environment (`D:\Argon_Code\Ropewalk\.venv`). No global installs and no changes to Windows or system settings.

## 4. Non-Destructive File Policy (NEVER DELETE ANYTHING)
- **NEVER DELETE ANYTHING.** Never run `del`, `rm`, `rmdir`, `Remove-Item`, `unlink`, `shutil.rmtree`, `os.remove`, or any equivalent deletion command or API (the single historical exception was the one-time proof test of the `icacls` lock on `_ORIGINALS`).
- **No destructive overwrites of versioned deliverables:** Never overwrite an existing deliverable or code file by replacing it. New versions must use new versioned filenames (`_v2`, `_v3`, etc.), leaving old versions intact. (Appending to `ACTIVITY_LOG.md` is permitted).
- **Use `_TRASH` for retirement:** If a temporary or obsolete file ever needs to be removed from active directories, move it (`Move-Item`) into `D:\Argon_Code\Ropewalk\_TRASH\` and inform the user.
- **Do not touch `_ORIGINALS/`:** The `_ORIGINALS/` directory and all files inside it are read-only and `icacls` delete-denied.

## 5. Hardware & CPU Cap (12 Workers Max)
- **Single-thread BLAS headers required:** Every Python script must begin with these exact environment variables before importing `numpy`, `scipy`, or any numerical library:
  ```python
  import os
  os.environ["OMP_NUM_THREADS"] = "1"
  os.environ["MKL_NUM_THREADS"] = "1"
  os.environ["OPENBLAS_NUM_THREADS"] = "1"
  os.environ["NUMEXPR_NUM_THREADS"] = "1"
  ```
- **Cap parallel workers at 12 cores (`N_CORES = 12`)** and set worker process priority to **Below Normal** (`psutil.BELOW_NORMAL_PRIORITY_CLASS`) so background runs never interfere with the user's video production work.
