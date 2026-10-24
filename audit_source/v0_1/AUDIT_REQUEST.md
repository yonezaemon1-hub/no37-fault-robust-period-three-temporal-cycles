# External independent audit request - No.37 v0.1

Please audit the submitted theorem, rather than treating the status labels or computations as proof. Report substantive defects before editorial issues. Do not infer novelty from the absence of a search hit.

## Requested separate verdicts

Report **PROOF**, **COMPUTATION**, **REFERENCES**, **NOVELTY**, and **PUBLICATION**, with the exact scope of each verdict. Use PASS / FAIL / PARTIAL / INCONCLUSIVE as appropriate. Distinguish a mathematical counterexample from a code or documentation defect.

## First checks

1. Run `python check_hashes.py` before modifying anything.
2. Read the model and the quantifier order in paper equations (1)-(2). Verify free-departure fastest duration, strict traversal, ordered pairs, static denominator, persistent phase replacement, and the no-fault option.
3. Run `python verify.py --output reviewer_evidence`. State the actual Python/OS and which tests were executed. Do not report a Windows test unless one was performed.
4. Reimplement at least one core calculation independently. The supplied two evaluators are separate methods, but were produced in the same workflow and are not an external independent audit.

## Priority proof questions

- Is the two-arc reduction valid under the chosen duration definition, including when walks are allowed?
- Does the identity F+B=3m-1+3q hold, with q counting equal adjacent phases?
- Does making two neighboring phases equal force the claimed lower bounds for n=4 and for every n>=5, including n=5?
- For n>=8 and 3 not dividing n, must some cyclic triple have a repeated phase? Can one change make it uniform, and can the complementary arc be oriented to force duration at least seven for the same ordered endpoints?
- For the canonical word lambda_i=i mod 3, verify **every wrap residue class**, both directions, faults internal to an arc, faults at an arc endpoint, and faults outside it.
- Check the reverse-arc argument carefully: ordinary internal pairs have sum four; an exceptional reverse wait three gives a pair sum five that cannot increase; an exceptional reverse wait one gives a pair sum three that may increase to six.
- Check m=1,2,3 separately. Verify no unproved large-m inequality is used for them.
- For C7, verify the exact word `(0,1,0,1,2,0,2)`, all seven cyclic triples, all four complements, both complementary orientations, and all fourteen nontrivial faults. Does the argument cover a fault outside the chosen short arc as well as inside it?
- Verify n=3,4,5 and that the theorem's disjoint cases exhaust all n>=3.

## Computation questions

- Validate the prefix-sum endpoint indexing and the definition of static distance.
- Check that the clock oracle computes minimum **duration**, not only earliest arrival from a fixed start time. It minimizes over all three starting thresholds.
- Verify phase normalization preserves the complete radius-one Hamming ball, especially faults on edge zero.
- Confirm every nontrivial replacement and the no-fault case are included, with no theorem-based pruning of the exhaustive optimization.
- The full normalized enumeration is through n=11. The full independent clock enumeration is through n=9, not n=11. Distinguish those scopes from the selected construction checks through n=36.
- Inspect the full compressed score arrays, histograms, optimal-label counts, C7 records, and claim-to-evidence mapping. Try to falsify the theorem rather than just reproduce its printed minimum.

## Novelty and claim questions

Consult both named STGR papers and search alternate/equivalent formulations: min-max phase labeling, one-coordinate Hamming-ball robustness, persistent periodic schedule errors, robust cyclic timetabling, ternary cyclic word constraints, temporal delay/modification problems, and fault-tolerant temporal stretch. The local-search STGR neighborhood is already known. Reversing its optimization quantifier alone is not evidence of historical novelty.

The residual audit's blocked full texts and incomplete coverage are listed in `RELATED_WORK.md`. Check whether a general theorem, a different terminology, an older exact cycle result, or a direct corollary subsumes this statement. Identify any precise overlap with the author's No.27 fault-free note. An internally correct theorem may still have NOVELTY=INCONCLUSIVE or FAIL.

## Requested audit output

For every defect, give the file/section, exact failed assertion, and a minimal counterexample or correction. For a proof PASS, state which cases and inequalities you checked and whether the proof is self-contained. For computational PASS, state the actual checks executed; do not inherit unexecuted tests. Preserve the submitted candidate and provide a separate audit report. Do not publish or change the theorem without explaining a concrete defect.

The current author-side decision is **PUBLICATION=HOLD**, **NOVELTY=INCONCLUSIVE**. Release to GitHub/Zenodo requires a later explicit decision after this audit.
