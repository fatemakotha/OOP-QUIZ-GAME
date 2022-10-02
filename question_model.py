class Question:
    def __int__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("dshf", "False")
print(new_q.text)