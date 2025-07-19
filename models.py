class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"学生ID: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}"

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"课程ID: {self.course_id}, 名称: {self.name}, 学分: {self.credit}"

class Grade:
    def __init__(self, student_id, course_id, score):
        self.student_id = student_id
        self.course_id = course_id
        self.score = score

    def __str__(self):
        return f"学生ID: {self.student_id}, 课程ID: {self.course_id}, 成绩: {self.score}"
