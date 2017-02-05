from src.google_foobar.P009_undercover_underground.solution_01 import answer
import unittest


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        N = 2
        K = 1
        expected = '1'
        self.assertEqual(expected, answer(N, K))

    def testcase_002(self):
        N = 3
        K = 2
        expected = '3'
        self.assertEqual(expected, answer(N, K))

    def testcase_003(self):
        N = 3
        K = 3
        expected = '1'
        self.assertEqual(expected, answer(N, K))

    def testcase_004(self):
        N = 4
        K = 3
        expected = '16'
        self.assertEqual(expected, answer(N, K))

    def testcase_005(self):
        N = 4
        K = 4
        expected = '15'
        self.assertEqual(expected, answer(N, K))

    def testcase_006(self):
        N = 4
        K = 5
        expected = '6'
        self.assertEqual(expected, answer(N, K))

    def testcase_007(self):
        N = 4
        K = 6
        expected = '1'
        self.assertEqual(expected, answer(N, K))

    def testcase_008(self):
        N = 8
        K = 17
        expected = '21426300'
        self.assertEqual(expected, answer(N, K))

    def testcase_009(self):
        N = 17
        K = 73
        expected = '4128587443786236413617992567808612814800'
        self.assertEqual(expected, answer(N, K))

    def testcase_010(self):
        N = 20
        K = 109
        expected = '11565167516449011402405138671907133965148772688639329910'
        self.assertEqual(expected, answer(N, K))


if __name__ == '__main__':
    unittest.main()
