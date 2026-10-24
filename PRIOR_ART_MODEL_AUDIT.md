# No.37 - Prior-art and model comparison

Ryutaro Yonezu / Yonezu Research Lab

24 October 2026. Supplement to the unchanged No.37 v0.1 audit candidate.

## Decision

The examined STGR/SPTGR texts, the SAND 2026 announcement, the indexed definitions of blackout-tolerant spanners, and the author's No.27 note do not directly supply the stated one-phase-fault cycle classification. This is the outcome of a scoped comparison, not a proof that no known result implies it.

**PROOF / COMPUTATION: PASS as reported by the external AI reviewer. REFERENCES: PARTIAL. NOVELTY: INCONCLUSIVE. PUBLICATION: HOLD.** No public release or author contact is authorized. The No.37 theorem, proofs, Python code, v0.1 evidence, and original ZIP have not been modified by this supplement.

The main progress in this pass is that the 58-page author-hosted JCSS manuscript was obtained and its definitions and local-search formulation could be checked directly. An additional closely related paper on perturbations and fastest eccentricity was also examined. The Bilò journal PDF could not be obtained in full, so full-text completion must not be claimed.

## 1. Candidate being compared

Let S(lambda) be the maximum, over ordered pairs of distinct cycle vertices, of fastest strict temporal-path duration divided by static cycle distance. For period three, duration is last traversal time minus first traversal time plus one, with free departure.

The objective is:

```text
beta_3(C_n) = min_lambda max_{d_H(lambda,mu)<=1} S(mu).
```

A change replaces one undirected physical edge's recurring phase; all its appearances change together. Routing and departure can adapt to the changed labeling. The no-fault option is included.

The proposed values remain 1 at n=3; 3/2 at n=4; 2 at n=5,7 and multiples of three at least six; 7/3 at all other n>=8.

## 2. Source-access record

| Work | Material actually examined | Exact locations relevant here | Remaining limit |
| --- | --- | --- | --- |
| Mertzios et al., MFCS 2025 | Primary publisher HTML and the arXiv v1 full text | Section 2; Section 7, Local Search STGR and its algorithmic theorem | Conference version is distinguished from the journal manuscript |
| Mertzios et al., JCSS 2026 | Complete 58-page PDF from the author's journal-publication link; relevant definitions, theorem statements, and local-search section examined | PDF pp. 5-6, Section 2 / Definition 1 / Observation 2; pp. 43-47, Section 7 / Theorem 30 | Author-hosted manuscript, not a byte-for-byte comparison with the publisher typeset PDF |
| Meusel et al., SAND 2026 | Complete six-page publisher HTML | Section 1 definitions; Section 3, especially Theorem 3.3; Section 4 | The announcement does not establish exhaustive coverage of its extended/follow-up work |
| Bilò et al., JCSS 2024 | Indexed text from the primary institutional PDF: Section 2, printed p. 4; publisher abstract; indexed Section 6 result | Definition of non-strict temporal path, hop distance, temporal alpha-spanner, blackout; existence of edge-fault-tolerant results | Full PDF retrieval returned 403, including an alternate institutional route; full theorem comparison remains incomplete |
| Yonezu, No.27 v1.0 | All three pages of the current supplied PDF | Section 1 model; main theorem; Section 4 scope | Author's own prior note is not evidence of historical novelty |
| Enright et al., TCS 2026 | Complete 23-page institutional PDF; Sections 1.2-1.3 and 5 examined | Printed p. 3, Definitions 1-2; printed p. 18, fastest eccentricity and TFaEP | Broader follow-up work is not exhausted |
| Füchsle et al., STACS 2022 | Complete 15-page publisher PDF; model/robustness definitions examined | Printed pp. 30:2-30:4 | Other algorithms/proofs are not independently re-audited |
| Füchsle et al., SAND 2022 | Complete 17-page publisher PDF; model and delay-announcement variants examined | Printed pp. 17:2-17:4 | Reachability result, not an exact periodic stretch theorem |

## 3. STGR/SPTGR: what is shared, and what the known results provide

Mertzios et al. use the same periodic single-phase edge model, strict traversal, free-departure fastest duration with the plus-one convention, and ratio to static distance. The phase set 1,...,Delta versus 0,...,Delta-1 is only a relabeling. The journal manuscript uses the acronym **SPTGR**; the conference paper uses **STGR**. Both names were included in the additional search.

The journal definition additionally writes an earliest-next-appearance condition on consecutive traversals. This does not change the minimum duration used by No.37: with the first traversal fixed, greedily taking each subsequent available edge finishes no later than any traversal of the same edge sequence that waits longer.

The Section 7 local-search problem fixes an input labeling and asks whether **some** labeling within k changed edges achieves a target stretch. The radius-one modification neighborhood in No.37 is therefore already established prior art. The paper's algorithmic result concerns evaluating an improvement neighborhood; its hardness results and general stretch bounds do not state the robust cycle closed form.

For a target b, the relevant quantifiers are:

```text
Ordinary STGR:        exists lambda, for all ordered pairs, exists a suitable path.
Local Search STGR:    given lambda, exists nearby mu, for all pairs, exists a path.
No.37 robust design:  exists lambda, for all nearby mu, for all pairs, exists a path.
```

This is an objective comparison. It is not a claim that a reversal of quantifiers is a new general principle, and does not by itself rule out a transformation from another known problem.

The source's universal pairwise bound specializes to 3-2/d at period three. Thus the familiar upper values for distance one, two, and three are 1, 2, and 7/3. Those local numbers must not be presented as new. No.37 still needs its matching robust lower bounds, the control of longer shortest arcs, and the small-cycle cases to obtain the full optimal classification.

**Scoped finding:** no parameter substitution in the examined stretch-bound, hardness, or local-search theorem statements supplies the exact min-max cycle formula.

## 4. Meusel et al.: the fraction 7/3 is not itself a novelty claim

The SAND announcement retains the ordinary STGR objective and studies realizability, hardness, and possible optimal stretch values. Its Theorem 3.3 states existence of instances with a specified lower bound for each period and integer construction parameter. At period three and parameter one, that bound is 7/3. This numerical value is consequently already present as a lower bound in the ordinary general-graph literature.

The theorem is existential over a family of instances and does not identify the input as every undirected C_n under one persistent phase replacement. It has no universal fault ball around an initially chosen labeling. Its restricted period-two/geodetic results also do not furnish the period-three robust cycle classification by direct specialization.

**Scoped finding:** no direct corollary was identified from the announced theorem statements. This does not rule out an unexamined extension or a nontrivial reduction.

## 5. Bilò et al.: three definition differences that matter

The primary indexed Section 2 defines temporal paths with **nondecreasing** labels. Their distance is the minimum **number of edges** in a temporal path. A temporal alpha-spanner preserves those distances relative to the given temporal graph. A blackout removes all edges carrying one chosen absolute-time label. Its guarantees compare the spanner and original temporal graph after the same blackout.

No.37 instead uses strictly increasing traversal times on a recurring schedule, elapsed duration, a static-distance denominator, and replacement of one recurring edge phase. These distinctions affect both feasible journeys and the objective; a shared word such as “stretch” does not establish equivalence.

The journal paper also has Section 6 on k-edge-fault-tolerant temporal spanners. It must not be described as considering only blackouts. The publisher abstract and an indexed Section 6 statement confirm this broader coverage. Deletion-based fault tolerance in a sparsification problem still differs from recurring phase replacement, but without full text this is not a complete theorem-level non-overlap audit.

**Scoped finding:** the definitions checked are not the same mathematical problem. Full-text overlap remains open.

## 6. Additional prior art that belongs in a future related-work revision

### Enright, Larios-Jones, Meeks, Pettersson (TCS 2026)

*Reachability in temporal graphs under perturbation* is more directly related to time-label errors than a blackout model. Definitions 1-2 allow at most zeta individual time-edge appearances to move within a bounded absolute-time interval. Section 5 also studies whether some allowed perturbation achieves a small fastest eccentricity from a specified source.

The paper uses strict temporal paths but defines duration without the plus one. For the same path, adding one preserves which path is fastest; the multiplicative ratios in No.37 nevertheless require the stated convention and cannot copy numerical thresholds without conversion. Its finite appearance-wise uncertainty, existential improvement objective, and single-source eccentricity differ from recurring edge-wise uncertainty, worst-case design, and all-pairs static-normalized stretch.

Setting zeta=1 does not directly represent shifting every periodic appearance of one physical edge. No direct result for the No.37 classification was identified in the examined sections.

### Füchsle, Molter, Niedermeier, Renken (STACS/SAND 2022)

The STACS work requires a fixed vertex route to remain realizable after bounded delays to individual time arcs; its precise schedule may adapt. The SAND companion allows routes to adapt when delays are announced before departure and also studies delays revealed during travel. In particular, universal disruptions followed by an existential adapting path are already studied. No.37 must not claim invention of that robustness quantifier pattern.

These models concern finite time-arc disruptions and connection/route feasibility, not assignment of recurring cycle phases to minimize worst all-pairs normalized duration. Their stated algorithmic results do not directly give the robust cycle values.

## 7. Comparison with No.27

No.27 and No.37 have the same underlying undirected cycle, period, waiting formula, ordered pairs, and duration convention. No.27 minimizes S(lambda); No.37 minimizes the maximum S(mu) over the radius-one fault ball.

The only immediate scalar implication of the ordinary optimum is beta_3(C_n) >= alpha_star(C_n,3), because the no-fault case belongs to every fault ball. The ordinary classification alone does not determine how good labelings and their neighbors are arranged, which is required for the robust optimum.

For example, at C4 the ordinary optimum in No.27 is 1 and the robust optimum proposed in No.37 is 3/2. The C7 word in No.37 and its complementary-arc proof are separate from the fault-free witnesses. No inconsistency between the two statements was found.

## 8. External review report: provenance and one count clarification

The user supplied a Claude review reporting PROOF=PASS and COMPUTATION=PASS, with Linux/Python 3.13.17 execution, 23/23 payload hashes, independent C++ optimization through n=16, independent path-model checks, and construction checks through n=39. These are **reviewer-reported** results. The C++ source, raw result tables, and logs were not attached in this turn, and this pass did not rerun that implementation. The official author-side evidence range remains n=3..11 until additional raw evidence is retained and checked.

One reported number needs a normalization label:

```text
sum_{n=3}^8 3^(n-1) * n * (n-1) = 162,378
sum_{n=3}^8 3^n     * n * (n-1) = 487,134
```

Thus 162,378 is exactly the number of ordered-pair checks after fixing lambda_0=0, not the literal unnormalized word count. This can still cover all words up to the proven global phase-shift symmetry. The reviewer should specify that normalization in its final report. It is a reporting clarification, not a mathematical counterexample or grounds to reverse PASS.

The reported n=7 failure of the canonical word is consistent with the exception already proved in v0.1. No theorem change follows from it.

The separate No.35 v0.3 addendum is received as a reviewer report: regression PASS; proof/computation/references PASS; novelty INCONCLUSIVE; release HOLD. Its ZIP was not re-opened in this No.37 comparison. The truncated hash `9a16aa90...` is not a full digest and has not been treated here as an independently verified file identity.

## 9. What can be stated now

Supported wording:

> The temporal model, stretch objective, relabeling neighborhood, temporal robustness, and time-label perturbations have established precedents. In the named primary texts and source sections examined, we did not identify an exact classification of the minimum worst-case stretch of period-three undirected cycles under one persistent arbitrary edge-phase replacement. This limited comparison does not establish historical novelty or priority.

Before revising the paper, add the perturbation/eccentricity and delay-robust routing references, specify Bilò's hop metric and non-strict paths, and record the external AI review as a report with its evidence limits. Retain v0.1 mathematical content and raw evidence unchanged. A complete Bilò theorem comparison and broader equivalent-formulation assessment remain outstanding.

**Publication remains HOLD.** This pass neither contacts authors nor releases any candidate.

## Source locators

1. Mertzios et al., MFCS 2025: https://doi.org/10.4230/LIPIcs.MFCS.2025.75 . Publisher HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.75/LIPIcs.MFCS.2025.75.html . Full arXiv text: https://arxiv.org/html/2504.14258v1 .
2. Mertzios et al., JCSS 160 (2026), 103814: https://doi.org/10.1016/j.jcss.2026.103814 . Author page: https://mertzios.net/ . The journal link on that page resolves to https://mertzios.net/papers/Jour/Jour_Temporal_Graph_Realization_Stretch.pdf . This 58-page PDF was obtained successfully even though the publisher and the web-reader path were blocked. Institutional metadata: https://livrepository.liverpool.ac.uk/3198251/ .
3. Meusel et al., SAND 2026: https://doi.org/10.4230/LIPIcs.SAND.2026.21 . Full publisher HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol373-sand2026/html/LIPIcs.SAND.2026.21/LIPIcs.SAND.2026.21.html .
4. Bilò et al., JCSS 141 (2024), 103495: https://doi.org/10.1016/j.jcss.2023.103495 . Indexed primary PDF: https://art.torvergata.it/retrieve/68c2a663-06f7-43ab-a00f-afd3be742129/JCSS_2024.pdf . Author bibliography: https://www.stefanoleucci.com/ . Full PDF not obtained.
5. Yonezu, *Exact Optimal Stretch of Period-Three Temporal Cycles*, Research Note No.27, v1.0, 15 October 2026. The supplied three-page PDF was read in full.
6. Jessica Enright, Laura Larios-Jones, Kitty Meeks, William Pettersson, *Reachability in temporal graphs under perturbation*, TCS 1083 (2026), 116138: https://doi.org/10.1016/j.tcs.2026.116138 . Primary institutional full PDF: https://eprints.gla.ac.uk/389464/2/389464.pdf .
7. Eugen Füchsle, Hendrik Molter, Rolf Niedermeier, Malte Renken, *Delay-Robust Routes in Temporal Graphs*, STACS 2022, article 30: https://doi.org/10.4230/LIPIcs.STACS.2022.30 .
8. Same authors, *Temporal Connectivity: Coping with Foreseen and Unforeseen Delays*, SAND 2022, article 17: https://doi.org/10.4230/LIPIcs.SAND.2022.17 .

## Retrieved-PDF fingerprints

These identify the exact downloaded source copies used for this pass; third-party source PDFs are not included in this supplement.

```text
25ab47d6ddbaf050da497622c7123b9dc97e04db86ca3e8273d09e466f2fd393  Mertzios author-hosted journal manuscript, 58 pages, 580750 bytes
eedc1507a34c8baf0c3d7f9c36b87bbff73fc005119b6f8574c53e520c00a9df  Enright et al. institutional journal PDF, 23 pages, 4073611 bytes
8cdcb17545134521e190a399de250c4bcbe8335cb55c31f965de54a6f755e114  Delay-Robust Routes, 15 pages, 795559 bytes
4d04ff330adebc30a5c6b18fa1470125946cdce335862094e5af02914eb0e038  Foreseen and Unforeseen Delays, 17 pages, 849960 bytes
```

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved for this original comparison note. Cited third-party works retain their respective rights and licenses.
