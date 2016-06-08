"""
Technique
- Sum all multiples of 3 + Sum of all multiples of 5 - Sum of all multiples of 15.
  Multiples of 15 should be subtracted as that has been added twice.

Note
- A comparatively better solution than the brute force algorithm.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 10 runs: Minimum - 0.62 sec, Average - 0.623 sec, Maximum 0.63 sec
- Not among the fastest or the slowest algorithms.
"""


def sum_of_multiples(multiple, n):
    result = 0
    for i in range(0, n, multiple):
        result = result + i

    return result


def answer(n):
    return sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)
