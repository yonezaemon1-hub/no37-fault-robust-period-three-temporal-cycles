# No.37 - Exact Fault-Robust Stretch of Period-Three Temporal Cycles

Ryutaro Yonezu / Yonezu Research Lab / public preprint v1.0 / 24 October 2026.

**Unrefereed. Novelty INCONCLUSIVE. No priority claim. All rights reserved.**

For period-three undirected cycles with at most one persistent arbitrary edge-phase replacement, the exact min-max fastest-duration/static-distance stretch is:

| n | beta_3(C_n) |
| --- | --- |
| 3 | 1 |
| 4 | 3/2 |
| 5,7 or n>=6 divisible by 3 | 2 |
| n>=8 not divisible by 3 | 7/3 |

Duration is last traversal time minus first traversal time plus one, with strict traversal and free departure. The no-fault case is included. Both orientations and both simple arcs are considered. Faults change an edge's recurring phase, not an individual occurrence.

The paper's mathematical sections are byte-identical in the LaTeX source to candidate v0.1. Release changes concern status, received external AI review and related-work coverage. `audit_source/v0_1/` preserves that complete original candidate and its historical HOLD labels. `PRIOR_ART_MODEL_AUDIT.md` is the scoped comparison completed before author release approval.

Offline verification (Python 3.12, standard library only):

```powershell
python .\check_hashes.py
python .\verify.py --output rerun_evidence
```

The author-side archive contains complete normalized enumeration n=3..11 (88,569 labelings), independent clock enumeration n=3..9 (9,837), construction checks through n=36, and 14 C7 changes plus no fault. An external AI reviewer reported additional independent C++ checks through n=16 and constructions through n=39. The additional C++ source/raw logs were not provided, so these are reported reviewer results rather than bundled author evidence. Linux/Python 3.12.14 release checks passed; Windows execution is unconfirmed.

The external AI review reports proof/computation PASS, references PARTIAL, novelty INCONCLUSIVE and PUBLICATION HOLD. The author explicitly instructed public release on 24 October 2026 as an unrefereed, qualified preprint. That instruction does not establish historical novelty or replace journal/conference peer review.

Research inquiries and earlier overlapping work: yonezaemon1+research@gmail.com
