import unittest
from ..class_definitions import student as my_student
"""
unit testing for student.py
"""

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = my_student.student('Treu', 'Brandon', 'Coding', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Brandon')
        self.assertEqual(self.student.last_name, 'Treu')
        self.assertEqual(self.student.major, 'Coding')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.first_name, 'Brampdon')
        self.assertEqual(self.student.last_name, 'Treu')
        self.assertEqual(self.student.major, 'Coding')
        self.assertEqual(self.student.gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Student: Treu, Brandon, Coding, 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            my_student.student('Tr3u', 'Brandon', 'Coding', 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            my_student.student('Treu', 'Brampton', 'Coding', 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            my_student.student('Treu', 'Brandon', 'Coding', 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            my_student.student('Treu', 'Brandon', 'Coding', 'Brandon')
            my_student.student('Treu', 'Brandon', 'Coding', 5.6)


if __name__ == '__main__':
    unittest.main()