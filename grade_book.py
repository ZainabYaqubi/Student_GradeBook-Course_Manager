class GradeBook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        student_id = student.get_id()
        self.students[student_id] = student

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].enroll(course_code)
            self.courses[course_code].add_student(student_id)
            return True
        return False

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
            return True
        return False

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id in self.students and course_code in self.courses:
            course = self.courses[course_code]
            assessment = course.find_assessment(assessment_title)
            if assessment:
                massage = assessment.grade_massage(score)
                print(f"Grade recorded for {student_id}. Result: {massage}")
                return True
        return False

    def calculate_average(self, student_id, course_code):
        if student_id in self.grades and course_code in self.grades[student_id]:
            student_course_grade = self.grades[student_id][course_code]
            scores = student_course_grade.value()
            if scores:
                average = sum(scores) / len(scores)
                return average
        return 0

    def search_student(self, keyword):
        found_students = []
        keyword = str(keyword).lower()
        for student in self.students.values():
            if keyword in str(student.get_id()) or keyword in str(student.get_name()).lower():
                found_students.append(student)
        return found_students

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

            if student_id in self.grades:
                del self.grades[student_id]

            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def get_result(self, average):
        passing_grade = 55
        if average >= passing_grade:
            return "Passed"
        return "Failed"

    def show_report(self, student_id, course_code):
        if student_id not in self.students:
            print("Student not found.")
            return False
        student = self.students[student_id]
        student.display_info()

        print("\nGrades:")

        if student_id in self.grades:
            for assessment, score in self.grades[student_id].items():
                print(f"{assessment}: {score}")

        print(f"\nAverage: {self.calculate_average(student_id, course_code):.2f}")

    def letter_grades(self, average):
        if average >= 90:
            return "A"

        elif average >= 80:
            return "B"

        elif average >= 70:
            return "C"

        elif average >= 60:
            return "D"

        else:
            return "F"

    