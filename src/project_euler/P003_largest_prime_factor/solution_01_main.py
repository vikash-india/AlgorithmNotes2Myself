import logging

from src.project_euler.P003_largest_prime_factor.solution_01 import answer


# Main
def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    N = 600851475143

    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    largest_prime_factor = answer(N)

    logging.info('Largest Factor is {0} '.format(largest_prime_factor))


# Call Main
if __name__ == '__main__': main()
