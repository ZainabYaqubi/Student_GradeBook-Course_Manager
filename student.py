class student:
    def __init__(self, student_id, name, email, courses):
        self.__student_id = student_id
        self.__name = name
        self.email = email
        self.courses = courses

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name