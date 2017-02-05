import logging

from src.project_euler.P004_largest_palindrome_product.solution_01 import answer


def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    print answer()


# Call Main
if __name__ == '__main__': main()
