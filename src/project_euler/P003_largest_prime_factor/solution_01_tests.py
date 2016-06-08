import unittest

from src.project_euler.P003_largest_prime_factor.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        N = 600851475143
        expected = 6857
        self.assertEqual(answer(N), expected)


if __name__ == '__main__':
    unittest.main()
