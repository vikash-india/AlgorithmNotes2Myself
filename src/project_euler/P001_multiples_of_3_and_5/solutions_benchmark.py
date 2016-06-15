import logging

from src.project_euler.P001_multiples_of_3_and_5.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: 0.000146, Average: 0.00018891, Maximum: 0.000269.
"""


def main():
    N = 1000
    benchmark(100, answer, N)

# Call Main
if __name__ == '__main__': main()
