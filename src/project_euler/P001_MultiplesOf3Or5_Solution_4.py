# Description: Sum of all Natural Numbers Less than 1000 Which are Multiples of 3 or 5

"""
Technique
- Sum of all multiples of 3 + Sum of all those multiples of 5 that are not multiple of 3
- This Multiples of 15 should be subtracted as that has been added twice.
- A Pythonic implementation which uses a list comprehension.

Note
- The optimisation that only those multiples of 5 are added which are not the multiple of 3 eliminates the need to
  subtract the multiples of 15.
- Among the slowest algorithms since lists are not very fast.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NUMBERS_BELOW_N = 10 million
- Time for 10 runs: Minimum - 0.9 sec, Average - 1.545 sec, Maximum 1.96 sec
- Not among the fastest or the slowest algorithms.
"""

NUMBERS_BELOW_N = 1000

def sum_of_multiples_of_3_and_5(n):
    result = sum([x for x in range(3, n, 3)])
    result = result + sum([x for x in range(5, n, 5) if x % 3 != 0])
    return result

# Main
def main():
    """Main function to test the above implementation. """

    NUMBERS_BELOW_N = 1000
    result = sum_of_multiples_of_3_and_5(NUMBERS_BELOW_N)
    print 'The sum of all natural numbers less than {0} which are multiples of 3 or 5 is {1}'.format(NUMBERS_BELOW_N, result)

# Call Main
main()