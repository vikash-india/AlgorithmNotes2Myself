# Description: Script to Generate Data Sets For Sorting Algorithms

import random
import logging

# Global Configuration
TOTAL_ROWS = 10
SORTED = False            # Overrides REVERSE_SORTED and RANDOM_NUMBERS
REVERSE_SORTED = False    # Overrides RANDOM_NUMBERS
RANDOM_NUMBERS = True     # Least Precedence
WRITE_TO_FILE = False

def configure_logging(write_to_file_enabled):
    """Configure Logging Based on Global Configurations."""

    # Set logging level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    level = logging.DEBUG

    # Do not print debug messages when writing to file is enabled.
    if (write_to_file_enabled):
        level = logging.INFO

    # Configure Log Level
    logging.basicConfig(level=level)

def generate_numbers():
    """Generate a list of numbers based on Global Configurations"""

    if SORTED:
        numbers = range(1, TOTAL_ROWS + 1)
    elif REVERSE_SORTED:
        numbers = range(TOTAL_ROWS, 0, -1)
    elif RANDOM_NUMBERS:
        numbers = range(1, TOTAL_ROWS + 1)
        random.shuffle(numbers)
        random.shuffle(numbers)
        random.shuffle(numbers)

    logging.debug(numbers)

    return numbers

def write_to_file(numbers, filename):
    """Write to file based on Global Configurations."""

    if WRITE_TO_FILE:
        logging.info('Writing data to file: {0}'.format(filename))

        with open(filename, 'w') as file_handle:
            for item in numbers:
                file_handle.write(str(item) + '\n')

def main():
    """Main function."""

    configure_logging(WRITE_TO_FILE)

    # Generate numbers based on configurations
    numbers = generate_numbers()

    # Write numbers to a file
    # Filenames Examples: dataset_10_reverse_sorted.txt, dataset_100_sorted.txt, dataset_1000_random.txt etc.
    filename="dataset/dataset_{0}_{1}.txt".format(TOTAL_ROWS, 'sorted' if SORTED else 'reverse_sorted' if REVERSE_SORTED else 'random')
    write_to_file(numbers, filename)

# Call Main
main()
