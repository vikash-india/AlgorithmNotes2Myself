# Description: Generate all Prime Numbers Between 1 and N using Optimised Sieve of Eratosthenes Algorithm

import math
import logging

"""
Note
1. This implementation generates all prime numbers between 1 and N using Optimised Sieve of Eratosthenes Algorithm.
2. Optimisation(s)
    - Instead of testing for all multiples of n, it is sufficient to mark the numbers in starting from n^2, as all the
      smaller multiples of n would have already been marked at that point. This means that the algorithm is allowed to
      terminate when n^2 is greater than LIMIT.
4. Limitation(s)
    - This implementation SHOULD NOT BE TRIED WITH A NUMBER GREATER THAN 100 Million.
"""

def sieve_of_eratosthenes(n):
    """Generate a list of all prime numbers between 1 and 'n' using optimised Sieve of Eratosthenes algorithm"""

    list_of_primes = [];

    list_of_numbers = [True] * n

    logging.debug("Square Root(N): {0}".format(int(math.floor(math.sqrt(n))) + 1))
    # for i = 2, 3, 4, ..., not exceeding Square Root(n)
    for i in range (2, int(math.floor(math.sqrt(n))) + 1):

        logging.debug("i={0}".format(i))

        if list_of_numbers[i - 1] == True:
            # for j = i^2, i^2+i, i^2+2i, i^2+3i not exceeding n
            for j in range(i * i, n + 1,  i):
                logging.debug("\tj={0}".format(j))
                list_of_numbers[j - 1] = False

    # Whatever indices greater than 1 is left as True are prime numbers
    for index, value in enumerate(list_of_numbers):
        if  index > 0 and value is True:
            list_of_primes.append(index + 1)

    return list_of_primes;

def main():
    """Main function to test the above implementation. """

    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    # Easily runs till 10 Million. Can ALSO run till 100 Million
    # CAUTION: DO NOT TRY FOR NUMBER GREATER THAN 100 BILLION
    N = 100
    list_of_primes = sieve_of_eratosthenes(N)
    print 'There are {0} prime numbers between 1 and {1}. The prime numbers are: \n{2}.'.format(len(list_of_primes), N,\
                                                                                       list_of_primes)
# Call Main
main()
