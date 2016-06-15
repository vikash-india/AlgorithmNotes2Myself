import unittest

from src.google_foobar.P007_binary_bunnies.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        seq = [5, 9, 8, 2, 1]
        expected = '6'
        self.assertEqual(answer(seq), expected)

    def testcase_002(self):
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = '1'
        self.assertEqual(answer(seq), expected)

    def testcase_003(self):
        seq = [5]
        expected = '1'
        self.assertEqual(answer(seq), expected)

    def testcase_004(self):
        seq = [5, 9]
        expected = '1'
        self.assertEqual(answer(seq), expected)

    def testcase_005(self):
        seq = [5, 9, 8, 2, 1, 10, 3]
        expected = '80'
        self.assertEqual(answer(seq), expected)

    def testcase_006(self):
        seq = [10, 8, 15, 6, 9, 4, 5]
        expected = '24'
        self.assertEqual(answer(seq), expected)

    def testcase_007(self):
        seq = [12, 6, 19, 15, 5]
        expected = '6'
        self.assertEqual(answer(seq), expected)

    def testcase_008(self):
        seq = [44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64]
        expected = '1'
        self.assertEqual(answer(seq), expected)


if __name__ == '__main__':
    unittest.main()
