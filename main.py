from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from grade_book import GradeBook

grade_book = GradeBook()
student_1 = Student("222", "Zainab", "zain@email.com")
student_2 = Student("11_2", "Mahdi", "mah@gmail.com")

grade_book.add_student(student_1)
grade_book.add_student(student_2)

course_1 = Course("PY101", "python programing")
grade_book.add_course(course_1)

grade_book.enroll_student("222", "PY101")
grade_book.enroll_student("11_2", "PY101")

assessment = Assessment("final project", 10)

print("===========================================")
print("        Student Grade_book Manager")
print("===========================================")

print("1. Add student")
print("2. View students")
print("3. Add course")
print("4. View courses")
print("5. Enroll student in course")
print("6. Add assessment")
print("7. Record grade")
print("8. View student report")
print("9. Delete student")
print("10. letter grade")
print("0. Exit")

continue_menu = True
while continue_menu:
    choice = int(input("Choose an option: \n"))
    if choice == 1:
        st_id = input("Enter student ID: ")
        name_st = input("Enter name: ")
        email_address = input("Enter email address: ")
        new_student = Student(student_id=st_id, name=name_st, email=email_address)
        grade_book.add_student(new_student)
        print("Student added successfully")

    elif choice == 2:
        for student in grade_book.students.values():
            student.display_info()

    elif choice == 3:
        cr_code = input("Enter course code: ")
        cr_name = input("Enter course name: ")
        new_course = Course(course_code=cr_code, course_name=cr_name)
        grade_book.add_course(new_course)
        print("Course added successfully")

    elif choice == 4:
        for course in grade_book.courses.values():
            print(course.course_code, "-", course.course_name)

    elif choice == 5:
        st_id = input("Enter student ID: ")
        cr_id = input("Enter course code: ")
        grade_book.enroll_student(student_id=st_id, course_code=cr_id)
        print("Student enrolled successfully")

    elif choice == 6:
        cr_code = input("Enter course code: ")
        qz_title = input("Enter quiz title: ")
        if cr_code in grade_book.courses:
            quiz = Quiz(title=qz_title, max_score=10)
            grade_book.courses[cr_code].add_assessment(quiz)
            print(f"Assessment added successfully to course {cr_code}")
        else:
            print(f"Course code {cr_code} does not exist")

    elif choice == 7:
        st_id = input("Enter student ID: ")
        co_code = input("Enter course code: ")
        asse_title = input("Enter assessment title: ")
        score_s = float(input("Enter score: "))
        grade_book.record_grade(student_id=st_id, course_code=co_code, assessment_title=asse_title, score=score_s)
        print("Grade recorded successfully! ")

    elif choice == 8:
        st_id = input("Enter student ID: ")
        cr_code = input("Enter course code: ")
        grade_book.show_report(student_id=st_id, course_code=cr_code)

    elif choice == 9:
        student_id = input("Enter student ID: ")
        grade_book.delete_student(student_id)

    elif choice == 10:
        letter_grade = int(input("Enter numerical average: "))
        result_letter = grade_book.letter_grades(letter_grade)
        print(f"The letter is {result_letter}")

    elif choice == 0:
        print("You are exit")
        continue_menu = False

    else:
        print("Invalid option")

