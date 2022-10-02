class QuizBrain:
    def __init__(self, question_number, question_list):
        self.question_number = 0
        self.question_list = question_list
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q. {self.question_number}{current_question.text}")