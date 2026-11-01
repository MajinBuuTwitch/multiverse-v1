# Session Handoff & Context Briefing (For New Antigravity Instance in `D:\Argon_Code\Ropewalk`)

**Read this file first.** It brings you completely up to speed on the user's project, hardware, rules, and the exact Part 1 setup steps that are already drafted and ready to execute.

---

## 1. The Project & User Context
- **User:** Gregory, screenwriter and YouTube creator (WickedAI). Beginner at coding; approves terminal commands as we go.
- **Goal:** Gregory has made a long documentary presenting a speculative multiverse model alongside real physics, accompanied by a public companion paper inviting physicists to try to break the model. We are doing the mathematical derivations and computational physics testing honestly—finding where the model fails just as plainly as where it passes.
- **Hardware & Environment:**
  - Windows PC: Intel i7-14700K (20 cores, 28 threads) + RTX 5080.
  - Active Workspace: `D:\Argon_Code\Ropewalk` (on the D: drive, strictly separate from Gregory's video work on the C: drive).
  - Subscription: Google AI Ultra (20x), with Overage / AI credits disabled.
  - Keep CPU usage capped at **12 worker processes** at **Below Normal priority**, with single-thread BLAS environment variables (`OMP_NUM_THREADS=1`, etc.) at the top of every Python script so Gregory can edit video simultaneously without lag.

---

## 2. Project Scope (in Stages)
- **Part 1 (Pre-Work Protections — DO THIS FIRST):**
  1. Write `GEMINI.md` in `D:\Argon_Code\Ropewalk`.
  2. Set up the `_ORIGINALS` file guard (`Copy-Item`, Read-Only attributes on `_ORIGINALS\*` and `MULTIVERSE_TESTS_v1.md`, plus `icacls` deny-delete `(OI)(CI)(D,DC)` on `_ORIGINALS`).
  3. Prove the file guard works by attempting to delete a file inside `_ORIGINALS` (`Remove-Item -Force` — the *only* time a delete command is ever run, strictly to prove the `icacls` lock works), confirm it fails with Access Denied, and log everything in `ACTIVITY_LOG.md`.
  4. **STOP and wait for Gregory to type `CONTINUE` before starting Stage 1.**
- **Stage 1 (Theoretical Derivations — No Code):**
  - Read `00_READ_FIRST.txt`, then `MULTIVERSE_ARGON_HANDOFF.txt`, then the equation sheet, `MULTIVERSE_TESTS_v1.md`, `DATASETS`, and the paper. **The handoff governs.**
  - Derive and tighten the model's equations mapping onto:
    1. Interacting dark energy (energy transfer between dark matter and dark energy),
    2. CPL dark energy parameters $(w_0, w_a)$,
    3. A delayed gravitational "shadow" for merging galaxy clusters,
    4. A spreading width for dark matter halos.
  - Flag every assumption and mark every equation as `[Established]` or `[Model Ansatz]`.
  - **Crucial Early-Universe Requirement:** Settle whether the leak (dark matter $\leftrightarrow$ dark energy transfer) acts only late in cosmic history. Compressed CMB priors assume a standard early universe; if the coupling matters before recombination, state so explicitly and specify what the full Boltzmann route (`CLASS`/`CAMB`) would require instead.
  - **Deliverable:** End Stage 1 with **one self-contained file**, `MULTIVERSE_STAGE1_EQUATIONS.md` (every equation, every assumption, parameter table, and $\Lambda\text{CDM}$ recovery limits). An independent reviewer (Claude) will read it cold with no access to this conversation before any code is written.
- **Stage 2 (Analysis Code in Python):**
  - Expansion-history fit against DESI DR2 BAO, supernova catalogs, and compressed CMB priors; merging-cluster offsets from published tables; galaxy rotation curves (SPARC).
- **Stage 3 (Run Fits):**
  - MCMC-style fits on this PC inside `.venv` (capped at 12 cores).
- **Stage 4 (Honest Reporting):**
  - Report results against pre-registered pass/fail tests in `MULTIVERSE_TESTS_v1.md`. No tuning after seeing data.

---

## 3. Approved Draft of `GEMINI.md` (Ready to Write in Part 1)

Write this exact content to `D:\Argon_Code\Ropewalk\GEMINI.md`:

```markdown
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
```

---

## 4. Approved File-Guard Commands (Ready to Execute in Part 1)

 Gregory has already reviewed these commands in the prior setup chat:

```powershell
# 1. Create _ORIGINALS and _TRASH directories
New-Item -ItemType Directory -Path "D:\Argon_Code\Ropewalk\_ORIGINALS" -Force
New-Item -ItemType Directory -Path "D:\Argon_Code\Ropewalk\_TRASH" -Force

# 2. Copy all starter files currently in the workspace root into _ORIGINALS
Get-ChildItem -Path "D:\Argon_Code\Ropewalk" -File | Where-Object { $_.Name -notin @("GEMINI.md", "ACTIVITY_LOG.md", "SESSION_BOOTSTRAP_HANDOFF.md") } | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination "D:\Argon_Code\Ropewalk\_ORIGINALS\$($_.Name)"
}

# 3. Mark every file inside _ORIGINALS as Read-Only
Get-ChildItem -Path "D:\Argon_Code\Ropewalk\_ORIGINALS" -File -Recurse | ForEach-Object {
    Set-ItemProperty -Path $_.FullName -Name IsReadOnly -Value $true
}

# 4. Mark the working copy of MULTIVERSE_TESTS_v1.md as Read-Only
Set-ItemProperty -Path "D:\Argon_Code\Ropewalk\MULTIVERSE_TESTS_v1.md" -Name IsReadOnly -Value $true

# 5. Deny Delete (D) and Delete Child (DC) on _ORIGINALS and everything inside it for the user's account
icacls "D:\Argon_Code\Ropewalk\_ORIGINALS" /deny "$($env:USERDOMAIN)\$($env:USERNAME):(OI)(CI)(D,DC)" /T

# 6. Prove the guard works: try to delete 00_READ_FIRST.txt in _ORIGINALS, confirm it fails with Access Denied
Remove-Item -Path "D:\Argon_Code\Ropewalk\_ORIGINALS\00_READ_FIRST.txt" -Force
Get-ChildItem -Path "D:\Argon_Code\Ropewalk\_ORIGINALS" | Select-Object Name, Length, Attributes
icacls "D:\Argon_Code\Ropewalk\_ORIGINALS"
```

---

## 5. Instructions for the New Instance on Turn 1
1. Confirm to Gregory that you have read `SESSION_BOOTSTRAP_HANDOFF.md` and that your active workspace is `D:\Argon_Code\Ropewalk`.
2. Since Gregory already reviewed the `GEMINI.md` draft and the file-guard commands above, ask if he wants you to execute Part 1 immediately (or execute it right away if his opening prompt says `CONTINUE` / tells you to apply Part 1).
3. After Part 1 finishes and `ACTIVITY_LOG.md` is updated, **STOP and wait for `CONTINUE`** before reading the physics files for Stage 1.
