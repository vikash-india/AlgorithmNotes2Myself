import logging

from src.project_euler.P002_even_fibonacci_numbers.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 1000 runs: Minimum: 3e-06, Average: 3.85e-06, Maximum: 1.7e-05.
"""


def main():
    upper_bound = 4000000
    benchmark(1000, answer, upper_bound)


# Call Main
if __name__ == '__main__': main()
