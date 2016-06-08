import logging
import random

"""
Note
1. This implementation tests a NUMBER for prime by choosing random values for 'a' and also limits the number of
   iterations.
2. Optimisation(s)
    - This implementation checks for 2 separately and then only check for all odd numbers between 3 and NUMBER. This
      improves the probability of success as even random numbers need not be considered.
    - This implementation chooses random ODD values of a between 3 and NUMBER.
    - This implementation limits the number of iterations instead of testing for all possible values of a.
3. Limitation(s)
    - This algorithm can easily test long prime numbers of 100 digits or more and is limited by the number of digits
      in prime numbers.
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

    for _ in xrange(1, iterations):
        # Return a randomly selected ODD element from the range 3 to number
        random_a = random.randrange(3, number, 2)
        tested_values_of_a.append(random_a)

        # Fermat's Little Theorem: a^p = a ( mod p )
        # Alternatively test a^(p-1) = 1 ( mod p )
        remainder = pow(random_a, number - 1, number)

        if(remainder != 1):
            logging.info(u'For a = {0}, {0}^({2} - 1) = {1} (mod {2}).'.format(random_a, remainder, number))

            # Definitely a Composite Number
            # print "Tested for {0}".format(tested_values_of_a)
            return False;

    # Probably a Prime Number
    # print "Tested for {0}".format(tested_values_of_a)
    return True
