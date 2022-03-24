"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../2_python_part_2'))
from task_classes import Homework, Teacher, Student
import datetime


class TestClasses(unittest.TestCase):
    def setUp(self) -> None:
        self.teacher = Teacher('Dmitry', 'Orlyakov')
        self.student = Student('Vladislav', 'Popov')

    def test_correct_names(self):
        self.assertEqual('Dmitry', self.teacher.last_name)
        self.assertEqual('Popov', self.student.first_name)

    def test_correct_homework(self):
        deadline: datetime.timedelta = datetime.timedelta(days=0)
        text: str = 'Learn functions'
        expired_homework = self.teacher.create_homework('Learn functions', 0)
        self.assertEqual(deadline, expired_homework.deadline)
        self.assertEqual(text, expired_homework.text)
        self.assertEqual(False, expired_homework.is_active())
        self.assertEqual(None, self.student.do_homework(expired_homework))

    def test_negative_days(self):
        deadline: datetime.timedelta = datetime.timedelta(days=0)
        negative_days_homework = self.teacher.create_homework('Negative', -5)
        negative_deadline: datetime.timedelta = datetime.timedelta(days=-5)
        self.assertEqual(negative_deadline, negative_days_homework.deadline)


if __name__ == '__main__':
    unittest.main()
