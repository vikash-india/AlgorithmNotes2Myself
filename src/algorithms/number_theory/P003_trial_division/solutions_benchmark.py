import logging

from src.algorithms.number_theory.P003_trial_division.solution_01 import prime_factors_using_trial_division
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 0.002497, Average: 0.00268113, Maximum: 0.003406.
"""


def main():
    benchmark(100, prime_factors_using_trial_division, 99999999999999999999)


# Call Main
if __name__ == '__main__': main()
