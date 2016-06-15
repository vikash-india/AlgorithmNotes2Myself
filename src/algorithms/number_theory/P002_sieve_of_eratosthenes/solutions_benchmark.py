import logging

from src.algorithms.number_theory.P002_sieve_of_eratosthenes.solution_01 import sieve_of_eratosthenes
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 1000 runs: Minimum: 0.000548, Average: 0.000606346, Maximum: 0.001258.
"""


def main():
    N = 10000
    benchmark(1000, sieve_of_eratosthenes, 1000)


# Call Main
if __name__ == '__main__': main()
