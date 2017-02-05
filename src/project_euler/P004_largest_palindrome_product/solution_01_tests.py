import unittest

from src.project_euler.P004_largest_palindrome_product.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        expected = 906609
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    unittest.main()
