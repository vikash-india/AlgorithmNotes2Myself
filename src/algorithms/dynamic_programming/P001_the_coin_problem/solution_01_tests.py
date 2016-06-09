import unittest

from src.algorithms.dynamic_programming.P001_the_coin_problem.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        coin_values = [1, 2, 3]
        coin_sum = 11
        expected = 4
        self.assertEqual(answer(coin_values, coin_sum), expected)

    def testcase_002(self):
        coin_values = [1, 2, 3]
        coin_sum = 9
        expected = 3
        self.assertEqual(answer(coin_values, coin_sum), expected)


if __name__ == '__main__':
    unittest.main()
