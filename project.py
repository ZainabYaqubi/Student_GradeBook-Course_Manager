from assessment import Assessment
class Project(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def grade_massage(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 70:
            return f"Excellent Project. Result: {percentage:.1f}%"
        elif percentage >= 30:
            return f"Project Submitted. Result: {percentage:.1f}%"
        else:
            return f"Project needs Improvement. Result: {percentage:.1f}%"

    def display_info(self):
        print(f"Project: {self.title}")
        print(f"Max Score: {self.max_score}")