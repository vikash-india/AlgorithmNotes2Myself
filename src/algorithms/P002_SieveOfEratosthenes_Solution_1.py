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
    - Another refinement is to initially list odd numbers only, (3, 5, ..., n), and count in increments of 2p in step 3,
      thus marking only odd multiples of p.
3. Limitation(s)
    - This implementation SHOULD NOT BE TRIED WITH A NUMBER GREATER THAN 100 Million.
"""

def sieve_of_eratosthenes(n):
    """Generate a list of all prime numbers between 1 and 'n' using optimised Sieve of Eratosthenes algorithm"""

    list_of_primes = [];

    # Initialise list with all EVEN items as False
    list_of_numbers = [True, False] * int(n/2)

    # Add the last item as True in case of ODD n
    # For n = 11, n/2.0 = 5.5, n/2 =  5, Ceil(5.5 - 5) = 1
    last_item = int(math.ceil(n/2.0 - n/2))
    if (last_item == 1):
        list_of_numbers.append(True)


    # Explicitly Set True for the even prime 2
    list_of_numbers[1] = True

    logging.debug("Square Root(N): {0}".format(int(math.floor(math.sqrt(n))) + 1))
    # for i = 2, 3, 4, ..., not exceeding Square Root(n)
    for i in range (3, int(math.floor(math.sqrt(n))) + 1, 2):

        logging.debug("i={0}".format(i))

        if list_of_numbers[i - 1] == True:
            # for j = i^2, i^2+i, i^2+2i, i^2+3i not exceeding n
            for j in range(i * i, n + 1,  2*i):
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
    UPPER_LIMIT = 200000000
    N = UPPER_LIMIT
    list_of_primes = sieve_of_eratosthenes(N)
    print 'There are {0} prime numbers between 1 and {1}. The prime numbers are: \n{2}.'.format(len(list_of_primes), N,\
                                                                                       "")
# Call Main
main()
