"""
Technique
- Sum of all multiples of 3 + Sum of all multiples of 5 - Sum of all multiples of 15
- Multiples of 15 should be subtracted as that has been added twice.
- This technique is a clever simplification of the arithmetic series formula where a = d

Notes:
    - This also runs in O(1) complexity and also consumes minimum amount of memory.
    - The formula is not very obvious in the first look.
    - Check P001_SumOfMultiplesOfThreeOrFive_7_Theory.png for the forum discussion on formula simplifications.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 100 runs: Minimum - 0.0 sec, Average - 0.0 sec, Maximum 0.0 sec
- Among the FASTEST algorithms. In fact, THE FASTEST with Big O(1) complexity.
"""


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2


def answer(n):
    n3 = (n - 1) // 3  # Floor of (n - 1) / 3
    n5 = (n - 1) // 5  # Floor of (n - 1) / 5
    n15 = (n - 1) // 15  # Floor of (n - 1) / 15

    return 3 * sum_of_natural_numbers(n3) + 5 * sum_of_natural_numbers(n5) - (15 * sum_of_natural_numbers(n15))
