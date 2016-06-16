import logging

from src.google_foobar.P001_pirates.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 9.99999999999e-07, Average: 2.11e-06, Maximum: 1.1e-05.
"""


def main():
    numbers = [22, 19, 65, 76, 60, 3, 15, 27, 53, 1, 23, 45, 38, 72, 54, 73, 29, 78, 47, 21, 0, 42, 63, 39, 13, 7,
               59, 28, 51, 36, 11, 18, 74, 6, 50, 8, 17, 33, 64, 4, 12, 9, 79, 24, 62, 56, 14, 70, 41, 69, 67, 5,
               48, 16, 71, 52, 58, 34, 68, 49, 40, 43, 26, 30, 32, 66, 35, 10, 20, 2, 61, 31, 77, 55, 37, 25, 46,
               75, 57, 44]
    benchmark(100, answer, numbers)


# Call Main
if __name__ == '__main__': main()
