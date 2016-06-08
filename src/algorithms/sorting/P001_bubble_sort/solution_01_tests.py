from src.algorithms.sorting.P001_bubble_sort.solution_01 import bubble_sort
import unittest


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(bubble_sort(numbers), expected)

    def testcase_002(self):
        numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(bubble_sort(numbers), expected)

    def testcase_003(self):
        numbers = [3, 7, 5, 4, 1, 6, 10, 8, 9, 2]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(bubble_sort(numbers), expected)


if __name__ == '__main__':
    unittest.main()
