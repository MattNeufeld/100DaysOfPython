class QuizBrain:

    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank
        self.score = 0

    def check_answer(self, user_Ans, correct_Ans):
        if user_Ans.lower() == correct_Ans.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong")
            print(f"The correct answer was {correct_Ans}")
        print(f"Current Score: {self.score}/{self.question_number}")

    def next_question(self):
        cQuestion = self.question_list[self.question_number]
        qAns = cQuestion.answer
        qText = cQuestion.text
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {qText} (True/False)?: ")
        self.check_answer(ans, qAns)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

