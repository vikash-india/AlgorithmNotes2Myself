from src.google_foobar.P000_template.solution_01 import answer
import unittest

class TestSolution(unittest.TestCase):
    def testcase_001(self):
        names = []
        expected = []
        self.assertEqual(answer(names), expected)

if __name__ == '__main__':
    unittest.main()
