import logging

from src.project_euler.P001_multiples_of_3_and_5.solution_01 import answer


def main():
    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    N = 1000
    result = answer(N)
    print 'The sum of all natural numbers less than {0} which are multiples of 3 or 5 is {1}'.format(N, result)


# Call Main
if __name__ == '__main__': main()
