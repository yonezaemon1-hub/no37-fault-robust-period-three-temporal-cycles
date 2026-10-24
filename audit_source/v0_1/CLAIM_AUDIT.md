# Claim and evidence audit - No.37 v0.1

Date: 24 October 2026. This is an internal production record, not an external reviewer report.

| Claim | Analytic basis | Finite evidence | Limit |
| --- | --- | --- | --- |
| Exact classification for every n>=3 | Theorem 1; lower bounds plus matching explicit constructions | All normalized assignments n=3..11 | Infinite quantification relies on proof |
| Two-direction identity F+B=3m-1+3q | Pairwise wait sums: 3 for unequal phases, 6 for equal phases | 9,840 words, lengths 1..8 | General proof in paper |
| One replacement increases path duration by <=2 at endpoints, <=3 internally | One wait bounded by 1..3; two-wait sums have fixed residue mod 3 | 147,624 replacements | General proof in paper |
| n=4 lower bound 3/2; n>=5 lower bound 2 | Equal two-edge arc plus slower complementary orientation | Global enumeration n=4..11 | Both orientations needed |
| n>=8, 3 not dividing n lower bound 7/3 | Repeated triple made uniform; complement length >=5 | Global enumeration n=8,10,11 | Fails as a lower-bound argument at n=7; handled separately |
| 3 divides n upper bound 2 | Canonical word; forward/reverse arc perturbations | Construction faults through n=36 | Proof covers arbitrary n |
| General canonical upper bound 7/3 | Wrap table; forward m+5 for m>=4; reverse <=2m+1; small m separately | Construction faults through n=36 | All three wrap residues included |
| C7 upper bound 2 for 0101202 | Uniform-triple exception and four unchanged complement checks | `c7_all_faults.json`, `c7_complement_table.json` | 14 nontrivial faults plus no fault |
| Arc and clock methods agree | Separate implementations with graph/clock oracle | All ordinary and robust scores n=3..9; 198,568 construction ordered-pair entries | Same production workflow; external audit pending |
| Python 3.12 compatibility | Executed Python 3.12.14, standard library only | `evidence/summary.json` | Linux execution only; Windows execution untested here |
| Exact result not identified in examined sources | Targeted primary-source/text/metadata audit | `RELATED_WORK.md` | Does not establish novelty or priority |

## Numerical counts and artifacts

The exhaustive arrays include every lambda_0=0 word, indexed exactly as described in the README. The complete robust value for a word is a maximum over its Hamming ball, using the full table of ordinary scores; no pruning by the proposed theorem is used. Direct evaluation of an empirical optimal witness is also checked for every n=3..11.

The clock evaluator does not import `arc_model.py`, `construction`, or `proposed_beta`; it uses a graph adjacency list and integer-clock advancement. The two methods share the intended model and phase-normalization principle. This is not evidence of external reviewer independence.

The paper's result cases have been made disjoint by explicitly restricting the divisible-by-three case to n>=6. This is a notation clarification of the original ordered piecewise statement, not a changed value at n=3.

## Decisions

PROOF: internally checked; external independent audit pending.

COMPUTATION: PASS within the exact stated scopes.

REFERENCES: PARTIAL (specific blocked full texts and unexamined equivalences remain).

NOVELTY: INCONCLUSIVE. No priority claim.

INDEPENDENT AUDIT: NOT PERFORMED.

PUBLICATION: HOLD. No GitHub/Zenodo release has been attempted.
