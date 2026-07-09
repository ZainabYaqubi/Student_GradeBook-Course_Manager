from assessment import Assessment

class Exam(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def grade_massage(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 55:
            return f"Passed Exam! Result: {percentage:.1f}%"
        else:
            return f"Failed Exam! Result: {percentage:.1f}%"

    def display_info(self):
        print(f"Exam: {self.title}")
        print(f"Mx Score: {self.max_score}")