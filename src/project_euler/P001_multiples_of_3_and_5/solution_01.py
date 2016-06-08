"""
Technique
- Brute force technique: Loop through all the numbers, test if divisible by 3 or 5 and sum it up.

Note
- The first and the most intuitive solution that comes to my mind.
- One of the slowest/worst solution possible.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 10 runs: Minimum - 2.69 sec, Average - 2.707 sec, Maximum 2.72 sec
- Among the slowest algorithms
"""


def answer(n):
    """Sum of the all natural numbers less than n that are multiples of 3 or 5"""

    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result = result + i

    return result
