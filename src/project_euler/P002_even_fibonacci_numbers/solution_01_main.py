import logging

from src.project_euler.P002_even_fibonacci_numbers.solution_01 import answer


# Main
def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    UPPER_BOUND = 4000000
    result = answer(UPPER_BOUND)
    print 'The sum of even fibionacci numbers less than {0} is {1}'.format(UPPER_BOUND, result)


# Call Main
main()

# Call Main
if __name__ == '__main__': main()
