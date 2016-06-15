import logging

from src.algorithms.sorting.P001_bubble_sort.solution_01 import bubble_sort
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 2.9e-05, Average: 3.53e-05, Maximum: 0.000305.
"""


def main():
    numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    benchmark(100, bubble_sort, numbers)


# Call Main
if __name__ == '__main__': main()
