import logging

from src.algorithms.number_theory.P001_fermat_primality_test.solution_02_best import is_fermat_prime
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 0.011689, Average: 0.01243977, Maximum: 0.014467.
"""


def main():
    benchmark(100, is_fermat_prime, 999998727899999, 1000)


# Call Main
if __name__ == '__main__': main()
