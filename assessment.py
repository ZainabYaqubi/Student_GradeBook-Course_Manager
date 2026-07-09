class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        percentage = (score / self.max_score) * 100
        return percentage

    def grade_massage(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 60:
            return f"Good Work!! Your result is {percentage:.1f}%."
        else:
            return f"Try Hard... You failed. Your result is {percentage:.1f}%."

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Max Score: {self.max_score}")