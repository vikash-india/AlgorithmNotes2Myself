# Description: Sum of all Even Fibonacci Numbers Less Than 4 Million

"""
Technique
- Similar logic as previous one with a slightly different implementation. No change in performance though.
- Since the series starts with 2 odd number, the third one will be even because it is result of two odd numbers. The
  next two will again be odd since one odd number gets added to an even number. In short, every third number in series
  will be event. Example
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
            a, b, c, a, b, c,  a,  b,  c,  a,  b, ...
- This simple observation can help us to solve this puzzle without the need to divide by 2 and find the reminder each
  time.
- Since we are interested in every 3rd number then why not compute the third number in the series directly. Starting
  from an two odd terms a, b, the series is:
            1, 1,     2,      3,       5,       8, 13, 21, 34, 55, 89, ...
            a, b, a + b, a + 2b, 2a + 3b, 3a + 5b, ...
- Compute the third term and add it to the sum. Compute fourth and fifth term and make it a and b. Now repeat.
            Third Term     = a + b
            Fourth Term    = a + 2b
            Fifth Term     = 2a + 3b

Note
- Not a very clear solution and moreover not much improvement in performance.

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: UPPER_BOUND = 1 Billion
- Time for 100 runs: Minimum - 0.0 sec, Average - 0.0 sec, Maximum 0.0 sec
"""
def sum_of_even_fibonacci_numbers(upper_bound):
    a, b = 1, 1
    result = 0
    while ((a + b) < upper_bound):

        # This is the 3rd term that directly gets added to the result
        result += (a + b)

        # a, b is set to fourth and fifth term so that sixth can be directly added to the result
        a, b = a + 2 * b, 2 * a + 3 * b

    return result

# Main
def main():
    """Main function to test the above implementation. """

    UPPER_BOUND = 4000000
    result = sum_of_even_fibonacci_numbers(UPPER_BOUND)
    print 'The sum of even fibionacci numbers less than {0} is {1}'.format(UPPER_BOUND, result)

# Call Main
main()
