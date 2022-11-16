import unittest
from


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student1.Student('Ovechkin', 'Alex', 'Goal Scoring', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.last_name, 'Ovechkin')
        self.assertEqual(self.student.major, 'Goal Scoring')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.last_name, 'Ovechkin')
        self.assertEqual(self.student.major, 'Goal Scoring')
        self.assertEqual(self.student.gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Student: Ovechkin, Alex, Goal Scoring, 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student1.Student('Ovechk7n', 'Alex', 'Goal Scoring', 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student1.Student('Ovechkin', 'Al3x', 'Goal Scoring', 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student1.Student('Ovechkin', 'Alex', 'G0al Scor1ng', 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student1.Student('Ovechkin', 'Alex', 'Goal Scoring', 'Alex')
            student1.Student('Ovechkin', 'Alex', 'Goal Scoring', 5.6)


if __name__ == '__main__':
    unittest.main()