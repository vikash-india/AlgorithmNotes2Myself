import unittest

from src.algorithms.number_theory.P001_fermat_primality_test.solution_02_best import is_fermat_prime


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        number = 2
        iteration = number
        expected = True
        self.assertEqual(is_fermat_prime(number, iteration), expected)

    def testcase_002(self):
        number = 99929
        iteration = 1000
        expected = True
        self.assertEqual(is_fermat_prime(number, iteration), expected)

    def testcase_003(self):
        number = 999983
        iteration = 1000
        expected = True
        self.assertEqual(is_fermat_prime(number, iteration), expected)

    def testcase_004(self):
        number = 825265
        iteration = 1000
        expected = False
        self.assertEqual(is_fermat_prime(number, iteration), expected)

    def testcase_005(self):
        number = 1033669
        iteration = 1000
        expected = False
        self.assertEqual(is_fermat_prime(number, iteration), expected)


if __name__ == '__main__':
    unittest.main()
