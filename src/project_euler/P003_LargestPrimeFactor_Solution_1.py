# Description: Write Here

import logging
import math

"""
Technique
- Loop from 2 till Square Root of N and keep dividing N by N

Note
- None

Instrumentation
- System Details: 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04
- Input Details: NA
- Time for 100 runs: Minimum - NA sec, Average - NA sec, Maximum NA sec
- Write Here
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
    N = 600851475143

    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.DEBUG)

    factors = prime_factors_using_trial_division(N)
    largest_factor = factors[-1]

    logging.info('Factors of {0} are {1}'.format(N, factors))
    logging.info('Largest Factor is {0} '.format(largest_factor))

# Call Main
main()
