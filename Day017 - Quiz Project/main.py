from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    newQ = Question(i["text"], i["answer"])
    question_bank.append(newQ)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nFinal Score: {quiz.score}/{quiz.question_number}")
