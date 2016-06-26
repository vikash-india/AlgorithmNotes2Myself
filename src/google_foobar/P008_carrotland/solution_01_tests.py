import unittest

from src.google_foobar.P008_carrotland.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        vertices = [[2, 3], [6, 9], [10, 160]]
        expected = 289
        self.assertEqual(answer(vertices), expected)

    def testcase_002(self):
        vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
        expected = 1730960165
        self.assertEqual(answer(vertices), expected)

    def testcase_003(self):
        vertices = [[0, 0], [0, 1], [1, 0]]
        expected = 0
        self.assertEqual(answer(vertices), expected)

    # Illustrated as problem_analysis_triangle_01.png
    def testcase_004(self):
        vertices = [[-1, -1], [1, 0], [0, 1]]
        expected = 1
        self.assertEqual(answer(vertices), expected)

    # Illustrated as problem_analysis_triangle_02.png
    def testcase_005(self):
        vertices = [[0, 0], [0, 10], [10, 0]]
        expected = 36
        self.assertEqual(answer(vertices), expected)

    # Illustrated as problem_analysis_triangle_03.png
    def testcase_006(self):
        vertices = [[1, 1], [4, 10], [10, 6]]
        expected = 31
        self.assertEqual(answer(vertices), expected)

    # Illustrated as problem_analysis_triangle_04.png
    def testcase_007(self):
        vertices = [[-5, 4], [4, 6], [3, -3]]
        expected = 39
        self.assertEqual(answer(vertices), expected)

    # Illustrated as problem_analysis_triangle_05.png
    def testcase_008(self):
        vertices = [[-5, -3], [5, -3], [0, 6]]
        expected = 40
        self.assertEqual(answer(vertices), expected)


if __name__ == '__main__':
    unittest.main()
