import logging

from src.algorithms.dynamic_programming.P001_the_coin_problem.solution_01 import answer

def main():
    # Set level from DEBUG, INFO, WARNING. ERROR, CRITICAL
    logging.basicConfig(level=logging.INFO)

    coin_values = [1, 2, 3]
    coin_sum = 11
    print answer(coin_values, coin_sum)


# Call Main
if __name__ == '__main__': main()
