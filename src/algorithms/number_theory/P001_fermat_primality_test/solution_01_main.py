import logging

from src.algorithms.number_theory.P001_fermat_primality_test.solution_01 import is_fermat_prime


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    # Sample Prime Numbers
    PRIME_NUMBER_03_DIGIT = 997                     # @UnusedVariable. Largest  3-digit prime number.
    PRIME_NUMBER_04_DIGIT = 9973                    # @UnusedVariable. Largest  4-digit prime number.
    PRIME_NUMBER_05_DIGIT = 99929                   # @UnusedVariable. Largest  5-digit prime number.
    PRIME_NUMBER_06_DIGIT = 999983                  # @UnusedVariable. Largest  6-digit prime number.
    PRIME_NUMBER_07_DIGIT = 9999991                 # @UnusedVariable. Largest  7-digit prime number.
    PRIME_NUMBER_08_DIGIT = 99999989                # @UnusedVariable. Largest  8-digit prime number.
    PRIME_NUMBER_09_DIGIT = 999999937               # @UnusedVariable. Largest  9-digit prime number.
    PRIME_NUMBER_10_DIGIT = 9999999929              # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_11_DIGIT = 99999999977             # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_12_DIGIT = 999999000001            # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_13_DIGIT = 9999999998987           # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_14_DIGIT = 99999999944441          # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_15_DIGIT = 999998727899999         # @UnusedVariable. Largest 10-digit prime number.
    PRIME_NUMBER_90_DIGIT = 374413471625854958269706803072259202131399386829497836277471117216044734280924224462969371 # @UnusedVariable.

    # Sample Carmichael Numbers
    CARMICHAEL_NUMBER_03_DIGIT = 561                # @UnusedVariable. N = 3 . 11 . 17
    CARMICHAEL_NUMBER_04_DIGIT = 1729               # @UnusedVariable. N = 7 . 13 . 19
    CARMICHAEL_NUMBER_05_DIGIT = 41041              # @UnusedVariable. N = 7 . 11 . 13 . 41
    CARMICHAEL_NUMBER_06_DIGIT = 825265             # @UnusedVariable. N = 5 . 7 . 17 . 19 . 73
    CARMICHAEL_NUMBER_07_DIGIT = 1033669            # @UnusedVariable. N = 7 . 13 . 37 . 307
    CARMICHAEL_NUMBER_08_DIGIT = None               # @UnusedVariable.
    CARMICHAEL_NUMBER_09_DIGIT = 321197185          # @UnusedVariable. N = 5 . 19 . 23 . 29 . 37 . 137
    CARMICHAEL_NUMBER_10_DIGIT = 5394826801         # @UnusedVariable. N = 7 . 13 . 17 . 23 . 31 . 67 . 73
    CARMICHAEL_NUMBER_11_DIGIT = 11346205609        # @UnusedVariable. N = 1237 . 2473 . 3709
    CARMICHAEL_NUMBER_12_DIGIT = 232250619601       # @UnusedVariable. N = 7 . 11 . 13 . 17 . 31 . 37 . 73 . 163
    CARMICHAEL_NUMBER_13_DIGIT = 9746347772161      # @UnusedVariable. N = 7 . 11 . 13 . 17 . 19 . 31 . 37 . 41 . 641
    CARMICHAEL_NUMBER_14_DIGIT = 26491881502801     # @UnusedVariable. N = 11 . 13 . 17 . 19 . 29 . 31 . 37 . 43 . 401
    CARMICHAEL_NUMBER_15_DIGIT = None               # @UnusedVariable.
    CARMICHAEL_NUMBER_90_DIGIT = None               # @UnusedVariable.

    # CAUTION: DO NOT TRY WITH A NUMBER GREATER THAN 7-DIGIT
    number = CARMICHAEL_NUMBER_06_DIGIT
    if(number is not None):
        result = is_fermat_prime(number)
        print '{0} is {1}Prime.'.format(number, '' if result else 'NOT ')

# Call Main
if __name__ == '__main__': main()
