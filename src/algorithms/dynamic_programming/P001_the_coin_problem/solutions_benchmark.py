import logging

from src.algorithms.dynamic_programming.P001_the_coin_problem.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 10000 runs: Minimum: 8.99999999998e-06, Average: 9.9473e-06, Maximum: 3.8e-05.
"""


def main():
    benchmark(10000, answer, [1, 2, 3], 11)


# Call Main
if __name__ == '__main__': main()
