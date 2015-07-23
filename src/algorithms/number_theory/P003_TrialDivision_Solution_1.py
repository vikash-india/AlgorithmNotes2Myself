# Description: Prime Factors Using Trial Division Algorithm

import logging
import math

"""
1. Note
    - Loop from 2 till Square Root of N and keep dividing N at every step.
2. Optimisation(s)
    - None
3. Limitation(s)
    - Do not try with numbers which has more than 15-digit prime factors.
"""

def prime_factors_using_trial_division(n):
    """Returns a list of all prime prime_factors of n"""

    prime_factors = []

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factor = i
            prime_factors.append(factor)
            n = n // i

    if n > 1:
        prime_factors.append(n)

    return prime_factors

# Main
def main():
    """Main function to test the above implementation. """
    NUMBER_01 = 600851475143         # 12-digit number with factors 71 x 839 x 1471 x 6857
    NUMBER_02 = 9007199254740992     # 20-digit number with factors 2^53
    NUMBER_03 = 9007199254740881     # 16-digit PRIME number.
    NUMBER_04 = 99999999999999999999 # 20-digit number with factors 3 x 3 x 41 x 101 x 271 x 3541 x 9091 x 27961

    # DO NOT TRY NUMBERS
    NUMBER_05 = 10000000000000000001 # 20-digit number with factors 11 x 909090909090909091

    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.DEBUG)

    n = NUMBER_04
    prime_factors = prime_factors_using_trial_division(n)
    logging.info('Prime Factors of {0} are {1}'.format(n, prime_factors))

# Call Main
main()
