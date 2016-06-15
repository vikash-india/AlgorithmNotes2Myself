import logging

from src.algorithms.number_theory.P003_trial_division.solution_01 import prime_factors_using_trial_division


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    NUMBER_01 = 600851475143  # @UnusedVariable. 12-digit number with factors 71 x 839 x 1471 x 6857
    NUMBER_02 = 9007199254740992  # @UnusedVariable. 20-digit number with factors 2^53
    NUMBER_03 = 9007199254740881  # @UnusedVariable. 16-digit PRIME number.
    NUMBER_04 = 99999999999999999999  # @UnusedVariable. 20-digit number with factors 3 x 3 x 11 x 41 x 101 x 271 x 3541 x 9091 x 27961

    # DO NOT TRY NUMBERS
    NUMBER_05 = 10000000000000000001  # @UnusedVariable. 20-digit number with factors 11 x 909090909090909091

    n = 12 * 25
    prime_factors = prime_factors_using_trial_division(n)
    logging.info('Prime Factors of {0} are {1}'.format(n, prime_factors))


# Call Main
if __name__ == '__main__': main()
