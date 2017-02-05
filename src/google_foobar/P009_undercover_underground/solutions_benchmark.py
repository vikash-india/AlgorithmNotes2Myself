import logging

from src.google_foobar.P009_undercover_underground.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: NA, Average: NA, Maximum: NA.
"""


def main():
    benchmark(100, answer, 1, 2)


# Call Main
if __name__ == '__main__': main()
