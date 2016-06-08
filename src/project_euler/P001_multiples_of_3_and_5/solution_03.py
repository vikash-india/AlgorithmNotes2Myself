"""
Technique
- Same technique as the previous one but implemented using Python language constructs instead of reinventing the wheel.
- Sum of all multiples of 3 + Sum of all multiples of 5 - Sum of all multiples of 15
- Multiples of 15 should be subtracted as that has been added twice.

Note
- None

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 10 runs: Minimum - 0.27 sec, Average - 0.28 sec, Maximum 0.3 sec
- Among the FASTER algorithms
"""


def answer(n):
    return sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15))
