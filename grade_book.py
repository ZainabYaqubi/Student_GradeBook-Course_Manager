from assessment import Assessment


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

