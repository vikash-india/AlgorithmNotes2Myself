# Description: Sum of all Even Fibonacci Numbers Less Than 4 Million

"""
Technique
- A simple and intuitive technique which is fast as well.

Notes
- None

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: UPPER_BOUND = 1 Billion
- Time for 100 runs: Minimum - 0.0 sec, Average - 0.0 sec, Maximum 0.0 sec
"""
def sum_of_even_fibonacci_numbers(upper_bound):
    a, b = 1, 1
    result = 0
    while b < upper_bound:
        a, b = b, b + a
        if b % 2 == 0:
            result += b
    return result

# Main
def main():
    """Main function to test the above implementation. """

    UPPER_BOUND = 4000000
    result = sum_of_even_fibonacci_numbers(UPPER_BOUND)
    print 'The sum of even fibionacci numbers less than {0} is {1}'.format(UPPER_BOUND, result)

# Call Main
main()
