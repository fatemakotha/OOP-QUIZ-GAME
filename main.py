from question_model import Question #from FILE question_model, import the CLASS named Question
from data import question_data #from the file named DATA, import the list named question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"] #taps into the KEY "text" of the Dictionary.
    question_answer = question["answer"] #taps into the KEY "answer" of the Dictionary
    new_question = Question(q_text=question_text, q_answer=question_answer) #takes the "text" and "answer" and makes a new question
    question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()