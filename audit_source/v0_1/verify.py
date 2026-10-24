"""Reproduce No.37 computational audit; Python 3.12, no dependencies/APIs.

Run: python verify.py --output rerun_evidence
Use --quick for the smaller documented smoke audit.
Original evidence is never overwritten by the default command.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import itertools
import json
from pathlib import Path
import platform
import sys
import time

import arc_model as arc
import clock_oracle as clock


def save_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')


def require(condition, context):
    if not condition:
        raise RuntimeError('FAIL: ' + str(context))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent / 'rerun_evidence')
    parser.add_argument('--quick', action='store_true')
    args = parser.parse_args()
    out = args.output.resolve()
    require(out != Path(__file__).resolve().parent / 'evidence', 'Choose a fresh output directory; evidence is immutable.')
    out.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    full = not args.quick
    summary = {'suite': 'full' if full else 'quick', 'python': sys.version,
               'platform': platform.platform(), 'utc_started': datetime.now(timezone.utc).isoformat(),
               'exhaustive': [], 'family': [], 'status': 'RUNNING'}
    max_n = 11 if full else 7
    oracle_max = 9 if full else 6
    pair_comparisons = 0
    ordinary_comparisons = 0
    robust_comparisons = 0

    # Verify the path identity and the exact one-label perturbation bound.
    identity_count = 0
    mutation_count = 0
    for m in range(1, 9 if full else 6):
        for word in itertools.product(range(3), repeat=m):
            equalities = sum(a == b for a, b in zip(word, word[1:]))
            require(arc.duration(word) + arc.duration(word[::-1]) == 3*m - 1 + 3*equalities, ('path identity', word))
            identity_count += 1
            for p in range(m):
                for replacement in range(3):
                    if replacement == word[p]:
                        continue
                    other = list(word)
                    other[p] = replacement
                    increase = arc.duration(other) - arc.duration(word)
                    bound = 0 if m == 1 else (2 if p in (0, m-1) else 3)
                    require(increase <= bound, ('mutation', word, p, replacement))
                    mutation_count += 1
    summary['path_identity_words'] = identity_count
    summary['path_mutations'] = mutation_count
    print(f'PASS path identity: {identity_count} words; {mutation_count} mutations', flush=True)

    for n in range(3, max_n + 1):
        ordinary, robust = arc.exhaustive(n)
        optimum = min(robust)
        require(optimum == arc.proposed_beta(n), ('optimum', n, optimum))
        optimal_indices = [i for i, value in enumerate(robust) if value == optimum]
        witness = arc.normalized_word(optimal_indices[0], n)
        require(arc.robust_score(witness)[0] == optimum, ('direct witness fault audit', n))
        record = {'n': n, 'normalized_labelings': len(robust),
                  'equivalent_unnormalized_labelings': 3*len(robust),
                  'optimum': str(optimum), 'optimal_count': len(optimal_indices),
                  'first_optimal_word': list(witness),
                  'robust_histogram': dict(Counter(map(str, robust))),
                  'clock_oracle_full_comparison': n <= oracle_max}
        if n <= oracle_max:
            c_ordinary, c_robust = clock.exhaustive(n)
            for i in range(len(robust)):
                word = arc.normalized_word(i, n)
                require(ordinary[i] == c_ordinary[word], ('ordinary disagreement', n, word))
                require(robust[i] == c_robust[word], ('robust disagreement', n, word))
            ordinary_comparisons += len(ordinary)
            robust_comparisons += len(robust)
        payload = {'n': n, 'index_rule': 'lambda_0=0; index=sum(lambda_i*3**(i-1),i=1..n-1)',
                   'ordinary': list(map(str, ordinary)), 'robust': list(map(str, robust))}
        (out / f'exhaustive_n{n:02d}.json.gz').write_bytes(gzip.compress((json.dumps(payload, separators=(',', ':'))+'\n').encode(), mtime=0))
        summary['exhaustive'].append(record)
        print(f'PASS exhaustive n={n}: {len(robust)} normalized labels, optimum={optimum}, clock={n <= oracle_max}', flush=True)

    last_n = 36 if full else 12
    oracle_ns = set(range(3, 13)) | {17, 24, 31, 36}
    for n in range(3, last_n + 1):
        word = arc.construction(n)
        result, witness = arc.robust_score(word)
        require(result == arc.proposed_beta(n), ('family', n, result))
        checked = 0
        if n in oracle_ns:
            for edge, new, modified in arc.fault_variants(word):
                d1, d2 = arc.distances(modified), clock.distances(modified)
                require(d1 == d2, ('distance matrix mismatch', n, edge, new))
                pair_comparisons += len(d1)
                checked += 1
        summary['family'].append({'n': n, 'labels': list(word), 'robust_stretch': str(result),
                                  'fault_scenarios_including_no_fault': 2*n+1,
                                  'clock_scenarios_compared': checked, 'worst_case_witness': witness})
    print(f'PASS constructions n=3..{last_n}; independent clock pair comparisons={pair_comparisons}', flush=True)

    exceptional = []
    seven = arc.construction(7)
    for edge, new, modified in arc.fault_variants(seven):
        value, pair = arc.score(modified)
        require(value <= 2, ('C7 fault', edge, new))
        require(arc.distances(modified) == clock.distances(modified), ('C7 clock fault', edge, new))
        exceptional.append({'edge': edge, 'new_phase': new, 'labels': list(modified),
                            'stretch': str(value), 'worst_pair': list(pair)})
    save_json(out / 'c7_all_faults.json', exceptional)
    triple_table = []
    for i in range(7):
        triple = [seven[(i+j) % 7] for j in range(3)]
        if len(set(triple)) != 3:
            complement = [seven[(i+j) % 7] for j in range(3, 7)]
            f, b = arc.duration(complement), arc.duration(complement[::-1])
            require(max(f, b) <= 6, ('C7 complement', i))
            triple_table.append({'start_edge': i, 'triple': triple, 'complement': complement,
                                 'forward': f, 'backward': b})
    require(len(triple_table) == 4, 'C7 exactly four repeated triples')
    save_json(out / 'c7_complement_table.json', triple_table)

    summary.update({'independent_ordinary_label_comparisons': ordinary_comparisons,
                    'independent_robust_label_comparisons': robust_comparisons,
                    'independent_family_pair_comparisons': pair_comparisons,
                    'c7_nontrivial_faults': len(exceptional)-1,
                    'counterexamples': 0, 'status': 'PASS',
                    'seconds': round(time.perf_counter() - started, 3)})
    save_json(out / 'summary.json', summary)
    print(f"PASS completed in {summary['seconds']} seconds; outputs: {out}", flush=True)


if __name__ == '__main__':
    main()
