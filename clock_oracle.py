"""Independent clock-time oracle; no imports from arc_model or proof formulas.

For each absolute start threshold 0,1,2, use time-dependent Dijkstra.
The next available edge is found by advancing an integer clock, not by
the modular waiting-time formula. Minimize duration over all thresholds.
"""
import heapq
import itertools
from fractions import Fraction


def distances(phases):
    n = len(phases)
    adjacency = [[] for _ in range(n)]
    for i, phase in enumerate(phases):
        j = (i + 1) % n
        adjacency[i].append((j, phase))
        adjacency[j].append((i, phase))
    output = {}
    infinity = 10 ** 9
    for source in range(n):
        fastest = [infinity] * n
        for threshold in range(3):
            arrival = [infinity] * n
            arrival[source] = threshold - 1
            queue = [(threshold - 1, source)]
            while queue:
                last, u = heapq.heappop(queue)
                if last != arrival[u]:
                    continue
                for v, phase in adjacency[u]:
                    clock = last + 1
                    while clock % 3 != phase:
                        clock += 1
                    if clock < arrival[v]:
                        arrival[v] = clock
                        heapq.heappush(queue, (clock, v))
            for v in range(n):
                if v != source:
                    fastest[v] = min(fastest[v], arrival[v] - threshold + 1)
        for v in range(n):
            if v != source:
                output[source, v] = fastest[v]
    return output


def score(phases):
    n = len(phases)
    answer = Fraction(1)
    for (s, t), duration in distances(phases).items():
        separation = abs(s - t)
        distance = min(separation, n - separation)
        answer = max(answer, Fraction(duration, distance))
    return answer


def exhaustive(n):
    """Tuple-keyed independent enumeration and Hamming-ball maximization."""
    ordinary = {}
    for tail in itertools.product(range(3), repeat=n - 1):
        phases = (0,) + tail
        ordinary[phases] = score(phases)
    robust = {}
    for phases, original in ordinary.items():
        largest = original
        for position in range(n):
            for replacement in range(3):
                modified = list(phases)
                modified[position] = replacement
                origin = modified[0]
                key = tuple((x - origin) % 3 for x in modified)
                largest = max(largest, ordinary[key])
        robust[phases] = largest
    return ordinary, robust
