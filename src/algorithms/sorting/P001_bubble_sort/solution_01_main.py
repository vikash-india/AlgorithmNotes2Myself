import logging
from src.algorithms.sorting.P001_bubble_sort.solution_01 import bubble_sort


def main():
    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    FILE_NAME = '../dataset/dataset_10_reversed.txt'

    # Read data set from the file
    with open(FILE_NAME, 'r') as file_handle:
        numbers = [int(line.rstrip('\n')) for line in file_handle]
        logging.info('Original Unsorted List: {0}'.format(numbers))

    result = bubble_sort(numbers)
    logging.info('Sorted List: {0}.'.format(result))


# Call Main
if __name__ == '__main__': main()
