from models import Student, Course, Grade
from database import Database

def main():
    # 创建数据库实例
    db = Database()

    # 添加示例学生
    student1 = Student("S001", "张三", 20)
    student2 = Student("S002", "李四", 19)
    db.add_student(student1)
    db.add_student(student2)

    # 添加示例课程
    course1 = Course("C001", "Python编程", 3)
    course2 = Course("C002", "数据库基础", 4)
    db.add_course(course1)
    db.add_course(course2)

    # 添加示例成绩
    grade1 = Grade("S001", "C001", 85)
    grade2 = Grade("S001", "C002", 90)
    grade3 = Grade("S002", "C001", 78)
    grade4 = Grade("S002", "C002", 88)
    db.add_grade(grade1)
    db.add_grade(grade2)
    db.add_grade(grade3)
    db.add_grade(grade4)

    # 显示学生信息
    print("\n学生信息：")
    for student_id in db.students:
        student = db.get_student(student_id)
        print(student)
        print(f"平均成绩: {db.calculate_student_average(student_id)}")
        print("各科成绩:")
        for grade in db.get_student_grades(student_id):
            course = db.get_course(grade.course_id)
            print(f"  {course.name}: {grade.score}")
        print()

if __name__ == "__main__":
    main()
