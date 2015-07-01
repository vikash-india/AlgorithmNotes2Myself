# Description: Test a Number for Prime Using Fermat's Primality Test

import random

"""
Note
1. This implementation tests a NUMBER for prime by choosing random values for 'a' and also limits the number of
   iterations.
2. Optimisation: This implementation checks for 2 separately and then only check for all odd numbers between 3 and
   NUMBER. This improves the probability of success as even random numbers need not be considered.
3. Optimisation: This implementation chooses random ODD values of a between 3 and NUMBER.
4. Optimisation: This implementation limits the number of iterations instead of testing for all possible values of a.
5. This algorithm can easily test long prime numbers of 100 digits or more.
"""
def is_fermat_prime(number, iterations):
    """Test the primality of a number using randomised algorithm."""

    tested_values_of_a = []

    # 1 is not prime
    if (number == 1):
        return False;

    # Test for 2 individually
    if (number == 2):
        return True;

    # Test for 2 separately so that only odd random numbers can be used improving the probability of success.
    if (number % 2 != 1):
        return False;

    for _ in range(1, iterations):
        # Return a randomly selected ODD element from the range 3 to number
        random_a = random.randrange(3, number, 2)
        tested_values_of_a.append(random_a)

        # Fermat's Little Theorem: a^p = a ( mod p )
        # Alternatively test a^(p-1) = 1 ( mod p )
        remainder = pow(random_a, number - 1, number)

        if(remainder != 1):
            print u'For a = {0}, {0}^({2} - 1) = {1} (mod {2}).'.format(random_a, remainder, number)

            # Definitely a Composite Number
            # print "Tested for {0}".format(tested_values_of_a)
            return False;

    # Probably a Prime Number
    # print "Tested for {0}".format(tested_values_of_a)
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

    ITERATIONS = 100                                # Number of Iterations

    number = PRIME_NUMBER_90_DIGIT
    if(number is not None):
        result = is_fermat_prime(number, ITERATIONS)
        print '{0} is {1}Prime.'.format(number, '' if result else 'NOT ')

# Call Main
main()
