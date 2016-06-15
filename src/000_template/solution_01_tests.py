import unittest

from src.google_foobar.P000_template.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        names = None
        expected = None
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    unittest.main()
