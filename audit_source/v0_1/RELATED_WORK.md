# Residual prior-art audit - 24 October 2026

## Scope and decision

Target: the **exact min-max one-persistent-phase-replacement optimum on an undirected cycle at period three**, as defined in the paper. No exact matching classification was identified in the material actually examined. **NOVELTY=INCONCLUSIVE; REFERENCES=PARTIAL.** Search absence is not proof of absence, and a difference in quantifier order does not establish a new scholarly contribution.

## Primary sources actually consulted

1. **George B. Mertzios, Hendrik Molter, Nils Morawietz, Paul G. Spirakis, Temporal Graph Realization with Bounded Stretch.** MFCS 2025, LIPIcs 345, article 75, 19 pages. Primary publisher HTML, including Section 2 definitions and Section 7 local search, examined.
   - https://doi.org/10.4230/LIPIcs.MFCS.2025.75
   - https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.75/LIPIcs.MFCS.2025.75.html
   - Journal-version metadata/abstract: JCSS 160 (2026), 103814, https://doi.org/10.1016/j.jcss.2026.103814 . Full publisher retrieval was blocked (403/redirect failure), so equivalence to the full journal version has not been verified.
   - Prior art: periodic single-phase edge labels, strict fastest-path duration, multiplicative stretch versus static distance, changing at most k edge labels, and the Local Search STGR Hamming neighborhood. Their local search asks whether some nearby labeling improves to a target stretch. The candidate uses the largest stretch in a radius-one ball and then minimizes over centers. This is a precise objective comparison, not a novelty conclusion.

2. **Julia Meusel, Nils Morawietz, Matthias Mueller-Hannemann, Klaus Reinhardt, Brief Announcement: Revisiting the Realizability of Periodic Temporal Graphs with Bounded Stretch.** SAND 2026, LIPIcs 373, article 21, 6 pages. Primary publisher HTML examined.
   - https://doi.org/10.4230/LIPIcs.SAND.2026.21
   - https://drops.dagstuhl.de/storage/00lipics/lipics-vol373-sand2026/html/LIPIcs.SAND.2026.21/LIPIcs.SAND.2026.21.html
   - Verified coverage includes period-two/geodetic realizability and the range of possible optimal stretch values. No claim is made to have exhausted longer versions, later work, or all references.

3. **Davide Bilo, Gianlorenzo D'Angelo, Luciano Guala, Stefano Leucci, Mirko Rossi, Blackout-tolerant temporal spanners.** JCSS 141 (2024), 103495.
   - https://doi.org/10.1016/j.jcss.2023.103495
   - Indexed primary institutional record/abstract (direct page retrieval was blocked): https://art.torvergata.it/handle/2108/321623
   - Journal record: https://art.torvergata.it/handle/2108/393673
   - An indexed primary institutional PDF extract defines a blackout as failure of all edges with a given time-label, and compares a temporal spanner after a blackout with the original temporal graph after that blackout. The abstract describes preservation of temporal distances despite such a failure. This differs from the candidate's persistent edge-phase replacement and static-distance denominator. Full PDF retrieval from the institutional endpoint and the journal publisher was blocked with 403; a complete theorem-to-theorem overlap audit was not performed.

4. **Ryutaro Yonezu, Exact Optimal Stretch of Period-Three Temporal Cycles.** Research Note No.27, unrefereed preprint v1.0, 15 October 2026, 3 pages. The supplied prior file was read in full. It uses the same free-departure strict duration convention and the fault-free objective. Its stated optimum is 1 for n=3,4; 3/2 for n=5 and even n>=6; 5/3 for odd n>=7. The No.37 proof does not invoke this result. This author's prior note is background, not third-party evidence of novelty.

## Search vocabulary used

Targeted web searches included:

- `"Temporal Graph Realization with Bounded Stretch"`
- `"Revisiting the Realizability of Periodic Temporal Graphs with Bounded Stretch"`
- `"temporal graph" "stretch" "robust" labeling`
- `"periodic temporal" "fault" stretch`
- `"stretched" "temporal" "local search" relabel`
- `"temporal cycle" "relabeling"`
- `"robust" "periodic temporal graphs" labeling`
- `"temporal graph" "adversarial" "relabeling"`
- `"robust timetabling" "stretch" cycles`
- `"fault" "stretched temporal graph realization"`
- `"temporal" "Hamming" "stretch"`
- `"periodic temporal" "robust" label`
- `"temporal graph" "phase" "reassignment"`
- `"fault tolerant" "periodic" "temporal graph" labeling stretch`
- `"Blackout-tolerant temporal spanners"` with PDF/definition refinements.

Two search backends were used. Irrelevant machine-learning and transportation search hits were not treated as evidence. No paid service or research computation on an external API was used. Literature retrieval is the only external lookup; verification scripts are offline.

## Mathematical equivalences to disclose

These are direct restatements of the candidate, not discoveries of additional prior literature:

- The objective is `min_lambda max_{Hamming(lambda,mu)<=1} S(mu)` on ternary cyclic words.
- For a target b, feasibility means that the whole closed radius-one Hamming ball around some labeling lies in the set of labelings with ordinary stretch at most b.
- The local lower-bound obstruction is a length-three cyclic edge word with a repeated color. Making it monochromatic takes at most one coordinate change. Every cyclic length-three window is rainbow if and only if the word is a cyclic repetition of a permutation of 0,1,2, requiring length divisible by three.
- The forward/backward identity and the two-wait residue argument are elementary consequences of modular waiting times. They are not claimed as historically new general principles.

## Remaining work for the independent reviewer

- Full-text check of the JCSS 2026 version and extended versions of the SAND paper.
- Complete theorem comparison with blackout/fault-tolerant temporal spanners, temporal delay/modification models, and robust periodic timetabling formulations.
- Search for older exact results stated as ternary cyclic-word constraints, robust schedule assignment, or Hamming-ball containment that could directly imply the cycle classification.
- Assess whether this narrow closed form is a direct known corollary, even if its exact title/notation is absent.

No assertion that this audit is complete, that the theorem is first, or that the broader robust temporal-graph problem is new is warranted.
