"""
Technique
- Sum of all multiples of 3 + Sum of all multiples of 5 - Sum of all multiples of 15
- Multiples of 15 should be subtracted as that has been added twice.
- A python implementation using the Sets

Note
- Using sets eliminates the need to worry about the multiple of 15 being double counted.
- Clearly among the slowest of algorithms since set itself will be slow.
- Moreover this will use a lot more RAM as it will store the set elements till the end for doing union.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 10 runs: Minimum - 1.61 sec, Average - 2.689 sec, Maximum 3.56 sec
- Among the slowest algorithms.
"""


def answer(n):
    return sum(set(range(0, n, 3)) | set(range(0, n, 5)))
