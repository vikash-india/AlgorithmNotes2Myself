# Description: Sum of all Even Fibonacci Numbers Less Than 4 Million

"""
Technique
- A slight improvement over the previous technique and a slight but unnoticeable improvement in performance as well.
- Since the series starts with 2 odd number, the third one will be even because it is the sum of two odd numbers. The
  next two will again be odd since one odd number gets added to an even number. In short, every third number in series
  will be even. Example
              1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
              a, b, c, a, b, c,  a,  b,  c,  a,  b, ...
- This simple observation can help us to solve this puzzle without the need to divide by 2 and find the reminder each
  time.

Note
- Simple and best solutions

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: UPPER_BOUND = 1 Billion
- Time for 100 runs: Minimum - 0.0 sec, Average - 0.0 sec, Maximum 0.0 sec
"""
def sum_of_even_fibonacci_numbers(upper_bound):
    a, b = 1, 2
    result = 0
    while b < upper_bound:
        result += b

        a, b = b, b + a # 2, 3
        a, b = b, b + a # 3, 5
        a, b = b, b + a # 5, 8 - This is the third number that needs to be added

    return result

# Main
def main():
    """Main function to test the above implementation. """

    UPPER_BOUND = 4000000
    result = sum_of_even_fibonacci_numbers(UPPER_BOUND)
    print 'The sum of even fibionacci numbers less than {0} is {1}'.format(UPPER_BOUND, result)

# Call Main
main()
