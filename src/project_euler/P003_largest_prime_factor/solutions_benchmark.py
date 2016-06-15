import logging

from src.project_euler.P003_largest_prime_factor.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 1000 runs: Minimum: 3e-06, Average: 3.842e-06, Maximum: 1.7e-05.
"""


def main():
    N = 600851475143
    benchmark(100, answer, N)


# Call Main
if __name__ == '__main__': main()
