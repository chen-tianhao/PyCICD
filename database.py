from models import Student, Course, Grade

class Database:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = []

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_id] = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_course(self, course_id):
        return self.courses.get(course_id)

    def get_student_grades(self, student_id):
        return [grade for grade in self.grades if grade.student_id == student_id]

    def get_course_grades(self, course_id):
        return [grade for grade in self.grades if grade.course_id == course_id]

    def calculate_student_average(self, student_id):
        grades = self.get_student_grades(student_id)
        if not grades:
            return 0
        return sum(grade.score for grade in grades) / len(grades)
