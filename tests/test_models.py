import unittest
from models import Student, Course, Grade

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("S001", "张三", 20)
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "张三")
        self.assertEqual(student.age, 20)

    def test_student_str(self):
        student = Student("S001", "张三", 20)
        expected = "学生ID: S001, 姓名: 张三, 年龄: 20"
        self.assertEqual(str(student), expected)

class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        course = Course("C001", "Python编程", 3)
        self.assertEqual(course.course_id, "C001")
        self.assertEqual(course.name, "Python编程")
        self.assertEqual(course.credit, 3)

    def test_course_str(self):
        course = Course("C001", "Python编程", 3)
        expected = "课程ID: C001, 名称: Python编程, 学分: 3"
        self.assertEqual(str(course), expected)

class TestGrade(unittest.TestCase):
    def test_grade_creation(self):
        grade = Grade("S001", "C001", 85)
        self.assertEqual(grade.student_id, "S001")
        self.assertEqual(grade.course_id, "C001")
        self.assertEqual(grade.score, 85)

    def test_grade_str(self):
        grade = Grade("S001", "C001", 85)
        expected = "学生ID: S001, 课程ID: C001, 成绩: 85"
        self.assertEqual(str(grade), expected)

if __name__ == '__main__':
    unittest.main()
