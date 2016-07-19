import unittest

from src.google_foobar.P000_template.solution_01 import answer


class TestSolution(unittest.TestCase):
    def testcase_001(self):
        expected = None
        names = None
        self.assertEqual(expected, answer())


if __name__ == '__main__':
    unittest.main()
