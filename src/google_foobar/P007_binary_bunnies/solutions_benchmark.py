import logging

from src.google_foobar.P007_binary_bunnies.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 2.7e-05, Average: 2.966e-05, Maximum: 6.8e-05
"""


def main():
    seq = [44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
    benchmark(100, answer, seq)


# Call Main
if __name__ == '__main__': main()
