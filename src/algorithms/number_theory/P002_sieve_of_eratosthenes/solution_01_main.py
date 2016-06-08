import logging

from src.algorithms.number_theory.P002_sieve_of_eratosthenes.solution_01 import sieve_of_eratosthenes


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    # Easily runs till 10 Million. Can ALSO run till 100 Million if given enough time.
    # CAUTION: DO NOT TRY FOR NUMBER GREATER THAN 100 BILLION
    UPPER_LIMIT = 200000000  # @UnusedVariable.

    N = 1000
    list_of_primes = sieve_of_eratosthenes(N)

    print 'Number of primes between 1 and {0}: {1}.'.format(N, len(list_of_primes))
    print 'The prime numbers are: {0}.'.format(list_of_primes)


# Call Main
if __name__ == '__main__': main()
