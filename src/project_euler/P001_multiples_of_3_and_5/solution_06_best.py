"""
Technique
- Sum of all multiples of 3 + Sum of all multiples of 5 - Sum of all multiples of 15 using Arithmetic Progression.
  Multiples of 15 should be subtracted as that has been added twice.
- A mathematical solution using the formula for the sum of an arithmetic progression.
        S(n) = n/2 * (a(1) + a(n))
        OR
        S(n) = n * (2 * a(1) + (n - 1) * d) / 2

Note
- A very mathematical way to solve the puzzle in O(1) complexity and also consumes minimum amount of memory.
- This is solution in linear time on the number of digits in n.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 100 runs: Minimum - 0.0 sec, Average - 0.0 sec, Maximum 0.0 sec
- The FASTEST algorithm possible.
"""


def sum_of_an_arithmetic_progression(a, d, n):
    return n * (2 * a + (n - 1) * d) / 2


def answer(n):
    n3 = (n - 1) // 3
    n5 = (n - 1) // 5
    n15 = (n - 1) // 15
    return sum_of_an_arithmetic_progression(3, 3, n3) + sum_of_an_arithmetic_progression(5, 5, n5) \
           - sum_of_an_arithmetic_progression(15, 15, n15)
