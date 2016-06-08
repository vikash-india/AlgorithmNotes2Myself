import unittest

from src.project_euler.P001_multiples_of_3_and_5.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        N = 1000
        expected = 233168
        self.assertEqual(answer(N), expected)


if __name__ == '__main__':
    unittest.main()
