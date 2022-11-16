"""
Brandon Treu
tests_average_scores.py

tests from the dictionary_test_example file
"""
import unittest
import dictionary_test_example


class MyTestCase(unittest.TestCase):

    def test_in_dict_true(self):
        d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        self.assertEqual(True, dictionary_test_example.in_dict(d, 'A'))

    def test_in_dict_false(self):
        d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        self.assertEqual(False, dictionary_test_example.in_dict(d, 'G'))


if __name__ == '__main__':
    unittest.main()