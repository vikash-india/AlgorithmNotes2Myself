from src.algorithms.number_theory.P003_trial_division.solution_01 import prime_factors_using_trial_division
import unittest


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        n = 600851475143
        expected = [71, 839, 1471, 6857]
        self.assertEqual(prime_factors_using_trial_division(n), expected)

    def testcase_002(self):
        n = 9007199254740992
        expected = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(prime_factors_using_trial_division(n), expected)

    def testcase_003(self):
        n = 9007199254740881
        expected = [9007199254740881]
        self.assertEqual(prime_factors_using_trial_division(n), expected)

    def testcase_004(self):
        n = 99999999999999999999
        expected = [3, 3, 11, 41, 101, 271, 3541, 9091, 27961]
        self.assertEqual(prime_factors_using_trial_division(n), expected)


if __name__ == '__main__':
    unittest.main()
