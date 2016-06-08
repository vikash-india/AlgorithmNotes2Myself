from src.project_euler.P002_even_fibonacci_numbers.solution_01 import answer
import unittest


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        N = 4000000
        expected = 4613732
        self.assertEqual(answer(N), expected)


if __name__ == '__main__':
    unittest.main()
