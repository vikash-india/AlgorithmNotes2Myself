import unittest

from src.google_foobar.P001_pirates.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        numbers = [1, 0]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_002(self):
        numbers = [1, 2, 1]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_003(self):
        numbers = [1, 3, 0, 1]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_004(self):
        numbers = [2, 1, 3, 2]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_005(self):
        numbers = [2, 2, 4, 4, 0]
        expected = 3
        self.assertEqual(answer(numbers), expected)

    def testcase_006(self):
        numbers = [2, 3, 1, 4, 5, 0]
        expected = 6
        self.assertEqual(answer(numbers), expected)

    def testcase_007(self):
        numbers = [1, 7, 1, 4, 5, 0, 7, 6]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_008(self):
        numbers = [19, 3, 1, 21, 22, 11, 13, 12, 8, 20, 32, 27, 2, 4, 23, 9, 36, 25, 39, 0, 15, 16, 38, 26, 37, 33, 7,
                   17, 29, 10, 34, 6, 35, 31, 24, 18, 30, 4, 14, 3]
        expected = 2
        self.assertEqual(answer(numbers), expected)

    def testcase_009(self):
        numbers = [5, 9, 5, 1, 6, 3, 6, 7, 2, 3, 0, 1]
        expected = 3
        self.assertEqual(answer(numbers), expected)

    def testcase_010(self):
        numbers = [12, 47, 7, 58, 53, 28, 9, 10, 5, 21, 27, 1, 13, 30, 38, 19, 18, 35, 57, 26, 36, 20, 33, 32, 6, 2, 24,
                   29, 8, 52, 54, 0, 44, 39, 23, 37, 4, 51, 40, 45, 55, 22, 34, 59, 43, 46, 49, 3, 14, 41, 42, 25, 56,
                   11, 15, 16, 50, 17, 48, 31]
        expected = 50
        self.assertEqual(answer(numbers), expected)

    def testcase_011(self):
        numbers = [22, 19, 65, 76, 60, 3, 15, 27, 53, 1, 23, 45, 38, 72, 54, 73, 29, 78, 47, 21, 0, 42, 63, 39, 13, 7,
                   59, 28, 51, 36, 11, 18, 74, 6, 50, 8, 17, 33, 64, 4, 12, 9, 79, 24, 62, 56, 14, 70, 41, 69, 67, 5,
                   48, 16, 71, 52, 58, 34, 68, 49, 40, 43, 26, 30, 32, 66, 35, 10, 20, 2, 61, 31, 77, 55, 37, 25, 46,
                   75, 57, 44]
        expected = 10
        self.assertEqual(answer(numbers), expected)


if __name__ == '__main__':
    unittest.main()
