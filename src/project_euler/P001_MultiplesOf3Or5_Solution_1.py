# Description: Sum of all Natural Numbers Less than 1000 Which are Multiples of 3 or 5

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
def sum_of_multiples_of_3_and_5(n):
    """Sum of the all natural numbers less than n that are multiples of 3 or 5"""

    result = 0
    for i in range(1, n):
        if(i % 3 == 0 or i % 5 == 0):
            result = result + i

    return result

# Main
def main():
    """Main function to test the above implementation. """

    NUMBERS_BELOW_N = 1000
    result = sum_of_multiples_of_3_and_5(NUMBERS_BELOW_N)
    print 'The sum of all natural numbers less than {0} which are multiples of 3 or 5 is {1}'.format(NUMBERS_BELOW_N, result)

# Call Main
main()
