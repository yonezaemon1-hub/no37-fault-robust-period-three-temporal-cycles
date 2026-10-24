# No.37 - Exact Fault-Robust Stretch of Period-Three Temporal Cycles

Ryutaro Yonezu / Yonezu Research Lab / 24 October 2026 / v0.1

**Internal audit candidate. Publication HOLD. Novelty INCONCLUSIVE.**

This bundle is for an external Claude audit. It has not been uploaded to GitHub or Zenodo. No external independent audit or journal/conference peer review has been completed.

## Mathematical statement

For an undirected cycle with strict temporal paths and one phase per edge in period three, choose a labeling, allow at most one persistent arbitrary edge-phase replacement, and measure the largest fastest-duration/static-distance ratio over ordered pairs. Minimize that worst case over initial labelings.

| Cycle length n | Proposed exact robust optimum |
| --- | --- |
| 3 | 1 |
| 4 | 3/2 |
| 5 or 7 | 2 |
| n >= 6 and 3 divides n | 2 |
| n >= 8 and 3 does not divide n | 7/3 |

Duration is **last traversal time - first traversal time + 1**. Departure is free. An equal-phase transition waits three time steps. Both orientations and both simple arcs are considered. The no-fault case is included. A fault changes one edge's recurring phase, not one individual occurrence. Static distances remain those of C_n.

The handed-over theorem and the C7 witness `(0,1,0,1,2,0,2)` are unchanged. Missing variables/ranges in the handoff have been restored from definitions and fresh computation. No earlier execution logs were available in that handoff; all bundled results were freshly generated in this session.

## Contents

- `No37_Fault_Robust_Stretch_v0_1.pdf`: English paper with complete analytic proof.
- `No37_Fault_Robust_Stretch_v0_1.tex`: matching editable LaTeX source.
- `arc_model.py`: exact two-arc evaluator and complete normalized enumeration.
- `clock_oracle.py`: separate graph/clock/Dijkstra evaluator; imports no arc code or theorem values.
- `verify.py`: reproducibility driver and finite falsification checks.
- `check_hashes.py`: payload-integrity checker.
- `evidence/`: original full-run summary, all normalized scores, and C7 data.
- `AUDIT_REQUEST.md`: instructions to the external reviewer.
- `RELATED_WORK.md`: residual source audit, equivalences, and limitations.
- `CLAIM_AUDIT.md`: claim-to-proof/evidence mapping and current decisions.
- `LICENSE.txt`: All rights reserved.
- `SHA256SUMS.txt`: hashes of every other shipped payload file.

## Run on Windows 10 / PowerShell / Python 3.12

No Python dependencies, external APIs, internet access, or paid services are required for verification. Run from the extracted folder. If the ZIP was downloaded to Downloads:

```powershell
$zip = "$env:USERPROFILE\Downloads\No37_Fault_Robust_Stretch_v0_1_20261024_Audit.zip"
$dest = "$env:USERPROFILE\Downloads\No37_Audit_v0_1"
Expand-Archive -LiteralPath $zip -DestinationPath $dest
Set-Location "$dest\No37_Fault_Robust_Stretch_v0_1"
python --version
python check_hashes.py
python verify.py --output rerun_evidence
```

Use `py -3.12` in place of `python` if needed. `--quick` reduces the audit to full enumeration through n=7, independent clock enumeration through n=6, construction tests through n=12, and path words through length five. The **default full run** is the run used for the paper. The default output path is next to the script; an explicit relative output path is relative to the current working directory. The original `evidence/` folder is protected against use as the verifier's output.

The supplied scripts were actually executed on Linux, Python 3.12.14. Windows 10 compatibility is based on their standard-library/path-neutral implementation and has **not** been confirmed on a Windows machine in this session. Runtime on the user's Windows PC is not asserted.

## Original full-run result

- Full normalized enumeration n=3..11: **88,569 assignments**, no theorem mismatch.
- Separate full clock enumeration n=3..9: **9,837 ordinary scores and 9,837 robust scores**, no disagreement.
- Construction checks n=3..36: all `2*n+1` fault scenarios at each n, including no fault.
- Full clock distance-matrix comparison for all construction faults at n=3..12,17,24,31,36: **198,568 ordered-pair entries**, no disagreement.
- Path identity: **9,840 words** of lengths 1..8.
- Single-phase path perturbations: **147,624** checks.
- C7: **14 nontrivial changes plus no fault**, all within stretch 2.
- Counterexamples within these scopes: **0**.

The full run took about nine seconds in the original execution environment. This is a historical measurement, not a cross-machine runtime promise. The analytic proof, not the finite checks, is responsible for the universal theorem.

`evidence/exhaustive_nNN.json.gz` contains arrays `ordinary` and `robust` of exact rational strings, indexed by

```text
lambda_0 = 0
index = sum(lambda_i * 3**(i-1), i=1,...,n-1)
```

No rotation, reflection, or general phase-permutation quotient is used. A global phase shift is normalized only by adding the same element of Z3 to every edge, which preserves both scores and Hamming balls. The gzipped files can be opened using Python's standard `gzip` and `json` modules.

Re-execution results should agree on deterministic numeric fields and all gzipped score files. The summary's platform, Python version, start time, and runtime will naturally differ. Do not regenerate `SHA256SUMS.txt` to hide a failed check. The manifest excludes itself; the external delivery hash file covers the final ZIP and paper.

## Current decisions

| Item | Status |
| --- | --- |
| Proof | Internally checked; external audit pending |
| Computation | PASS within stated scope |
| References | PARTIAL |
| Novelty / priority | INCONCLUSIVE; no priority claim |
| External independent audit | NOT PERFORMED |
| Publication | HOLD |

The separate oracle is methodological separation within one production workflow. It is not independent authorship or external review. Do not publish this candidate on the basis of these internal checks alone.

Research contact: yonezaemon1+research@gmail.com

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
