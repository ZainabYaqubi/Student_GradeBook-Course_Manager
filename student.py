class Student:
    def __init__(self, student_id, name, email):
        self.__student_id = student_id
        self.__name = name
        self.email = email
        self.courses =[]

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_email(self, n_email):
        if "@" in n_email and "." in n_email:
            self.email = n_email
            return True
        else:
            return False

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
            return True
        return False

    def display_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Student Name: {self.__name}")
        print(f"Email: {self.email}")
        print(f"Enrolled Courses: {self.courses}")