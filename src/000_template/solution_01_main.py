import logging

from src.P000_template.solution_01 import answer


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    answer([])


# Call Main
if __name__ == '__main__': main()
