"""Exact cycle-arc evaluator. Python 3.12+, standard library only.

Edges e_i = {i, i+1}; phases lie in {0,1,2}; traversal times
strictly increase. Duration is last time - first time + 1.
"""
from fractions import Fraction


def wait(a, b):
    return (b - a - 1) % 3 + 1


def duration(phases):
    return 1 + sum(wait(a, b) for a, b in zip(phases, phases[1:]))


def distances(labels):
    """Return all ordered-pair fastest durations using the two simple arcs."""
    labels = tuple(labels)
    n = len(labels)
    assert n >= 3 and all(x in (0, 1, 2) for x in labels)
    forward = [0]
    backward = [0]
    for i in range(2 * n):
        a, b = labels[i % n], labels[(i + 1) % n]
        forward.append(forward[-1] + wait(a, b))
        backward.append(backward[-1] + wait(b, a))
    result = {}
    for u in range(n):
        for k in range(1, n):
            v = (u + k) % n
            cw = 1 + forward[u + k - 1] - forward[u]
            ccw = 1 + backward[u + n - 1] - backward[u + k]
            result[u, v] = min(cw, ccw)
    return result


def score(labels):
    n = len(labels)
    num, den = 1, 1
    worst = (0, 1)
    for (u, v), t in distances(labels).items():
        k = (v - u) % n
        d = min(k, n - k)
        if t * den > num * d:
            num, den, worst = t, d, (u, v)
    return Fraction(num, den), worst


def fault_variants(labels):
    """No fault followed by exactly 2*n nontrivial one-edge changes."""
    labels = tuple(labels)
    yield None, None, labels
    for edge, old in enumerate(labels):
        for new in range(3):
            if new != old:
                changed = list(labels)
                changed[edge] = new
                yield edge, new, tuple(changed)


def robust_score(labels):
    value = Fraction(0)
    record = None
    for edge, new, changed in fault_variants(labels):
        current, pair = score(changed)
        if current > value:
            value = current
            record = {"edge": edge, "new_phase": new,
                      "changed_labels": list(changed), "pair": list(pair)}
    return value, record


def normalized_word(index, n):
    """lambda_0=0; index = sum(lambda_i*3**(i-1), i=1,...,n-1)."""
    labels = [0]
    for _ in range(n - 1):
        labels.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(labels)


def normalized_index(labels):
    shift = labels[0]
    total, power = 0, 1
    for x in labels[1:]:
        total += ((x - shift) % 3) * power
        power *= 3
    return total


def exhaustive(n):
    """Full normalized label space; no theorem-dependent pruning."""
    size = 3 ** (n - 1)
    ordinary = [score(normalized_word(i, n))[0] for i in range(size)]
    robust = []
    for i in range(size):
        labels = normalized_word(i, n)
        best = ordinary[i]
        for _, _, changed in fault_variants(labels):
            best = max(best, ordinary[normalized_index(changed)])
        robust.append(best)
    return ordinary, robust


def construction(n):
    if n == 4:
        return (0, 1, 0, 1)
    if n == 7:
        return (0, 1, 0, 1, 2, 0, 2)
    return tuple(i % 3 for i in range(n))


def proposed_beta(n):
    if n == 3:
        return Fraction(1)
    if n == 4:
        return Fraction(3, 2)
    if n in (5, 7) or n % 3 == 0:
        return Fraction(2)
    return Fraction(7, 3)
