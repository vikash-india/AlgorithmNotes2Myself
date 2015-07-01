# Description: Test a Number for Prime Using Fermat's Primality Test

"""
Note
1. This implementation tests a NUMBER for prime using all possible values of 'a' between 1 and NUMBER.
2. Optimisation: This implementation checks for 2 separately and then only checks for all odd numbers between 3 and
   NUMBER.
3. This algorithm SHOULD NOT BE TRIED WITH A NUMBER GREATER THAN 7-DIGIT or 8-DIGIT numbers as it might take eternity
   to finish.
"""

def is_fermat_prime(number):
    """Test a Number for Prime Using Fermat's Primality Test"""

    # 1 is not prime
    if (number == 1):
        return False;

    # Test for 2 individually
    if (number == 2):
        return True;

    # Test for 2 separately so that only odd numbers need to be tested in a loop saving half iterations.
    if (number % 2 != 1):
        return False;

    # Optimisation: Test for all odd numbers starting 3
    for i in range(3, number, 2):
        # Fermat's Little Theorem: a^p = a ( mod p )
        # Alternatively test a^(p-1) = 1 ( mod p )
        remainder = pow(i, number - 1, number)
        if(remainder != 1):
            print u'For a = {0}, {0}^({2} - 1) = {1} (mod {2}).'.format(i, remainder, number)

            # Definitely a Composite Number
            return False;

    # Probably a Prime Number
    return True

def main():
    """Main function to test the above implementation. """

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
    PRIME_NUMBER_90_DIGIT = 374413471625854958269706803072259202131399386829497836277471117216044734280924224462969371

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
    number = CARMICHAEL_NUMBER_04_DIGIT
    if(number is not None):
        result = is_fermat_prime(number)
        print '{0} is {1}Prime.'.format(number, '' if result else 'NOT ')

# Call Main
main()
