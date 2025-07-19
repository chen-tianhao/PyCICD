import unittest
from models import Student, Course, Grade
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.student = Student("S001", "张三", 20)
        self.course = Course("C001", "Python编程", 3)
        self.grade = Grade("S001", "C001", 85)

    def test_add_and_get_student(self):
        self.db.add_student(self.student)
        retrieved_student = self.db.get_student("S001")
        self.assertEqual(retrieved_student.name, "张三")
        self.assertEqual(retrieved_student.age, 20)

    def test_add_and_get_course(self):
        self.db.add_course(self.course)
        retrieved_course = self.db.get_course("C001")
        self.assertEqual(retrieved_course.name, "Python编程")
        self.assertEqual(retrieved_course.credit, 3)

    def test_add_and_get_grade(self):
        self.db.add_grade(self.grade)
        grades = self.db.get_student_grades("S001")
        self.assertEqual(len(grades), 1)
        self.assertEqual(grades[0].score, 85)

    def test_calculate_student_average(self):
        self.db.add_grade(self.grade)
        self.db.add_grade(Grade("S001", "C002", 95))
        average = self.db.calculate_student_average("S001")
        self.assertEqual(average, 90)

    def test_get_course_grades(self):
        self.db.add_grade(self.grade)
        self.db.add_grade(Grade("S002", "C001", 75))
        grades = self.db.get_course_grades("C001")
        self.assertEqual(len(grades), 2)
        self.assertEqual(grades[0].score, 85)
        self.assertEqual(grades[1].score, 75)

if __name__ == '__main__':
    unittest.main()
