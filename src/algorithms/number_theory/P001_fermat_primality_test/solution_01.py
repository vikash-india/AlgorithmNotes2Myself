import logging

"""
Note
1. This implementation tests a NUMBER for prime using all possible values of 'a' between 1 and NUMBER.
2. Optimisation
    - This implementation checks for 2 separately and then only checks for all odd numbers between 3 and NUMBER.
3. Limitation(s)
    - This algorithm SHOULD NOT BE TRIED WITH A NUMBER GREATER THAN 7-DIGIT or 8-DIGIT numbers as it might take eternity
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
    for i in xrange(3, number, 2):
        # Fermat's Little Theorem: a^p = a ( mod p )
        # Alternatively test a^(p-1) = 1 ( mod p )
        remainder = pow(i, number - 1, number)
        if(remainder != 1):
            logging.info(u'For a = {0}, {0}^({2} - 1) = {1} (mod {2}).'.format(i, remainder, number))

            # Definitely a Composite Number
            return False;

    # Probably a Prime Number
    return True
