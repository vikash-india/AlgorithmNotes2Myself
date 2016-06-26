import logging

from src.google_foobar.P008_carrotland.solution_01 import answer
from src.tools.instrumentation import benchmark

"""
Note
- Instrumentation on a system with 8x Intel Core i7-3630QM CPU @ 2.40GHz, 16GB RAM, Ubuntu 14.04.
- Time (In seconds) for 100 runs: Minimum: NA, Average: NA, Maximum: NA.
- Time (In seconds) for 100 runs: Minimum: 5e-06, Average: 1.098e-05, Maximum: 6.5e-05.
"""


def main():
    vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
    expected = 1730960165
    benchmark(100, answer, vertices)


# Call Main
if __name__ == '__main__': main()
