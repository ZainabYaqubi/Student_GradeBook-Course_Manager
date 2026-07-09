from assessment import Assessment
class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def grade_massage(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 70:
            return f"Great quiz result: {percentage:.1f}%"
        else:
            return f"Need more practice: {percentage:.1f}%"

    def display_info(self):
        print(f"Quiz 1: {self.title}")
        print(f"Max Score: {self.max_score}")