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

    # Test for 2 separately so that only ODD numbers can be tested in the loop
    while n % 2 == 0:
        factor = 2
        prime_factors.append(factor)
        n = n // 2

    # Test only for ODD numbers starting with 3
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        # logging.debug("i = {0}".format(i))
        while n % i == 0:
            factor = i
            prime_factors.append(factor)
            n = n // i
            logging.debug("Factor = {0}, N = {1}".format(i, n))

        # All factors have been found if N is reduced to 0.
        if n == 1:
            break

    # If no factor has been found then N is PRIME and the only prime factor of itself.
    if n > 1:
        prime_factors.append(n)

    return prime_factors


def answer(n):
    prime_factors = prime_factors_using_trial_division(n)
    return prime_factors[-1]
