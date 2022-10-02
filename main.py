from question_model import Question #from FILE question_model, import the CLASS named Question
from data import question_data #from the file named DATA, import the list named question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"] #taps into the KEY "text" of the Dictionary.
    question_answer = question["correct_answer"] #taps into the KEY "answer" of the Dictionary
    new_question = Question(q_text=question_text, q_answer=question_answer) #takes the "text" and "answer" and makes a new question
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
