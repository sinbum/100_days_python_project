class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        quiz_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"""Q.{self.question_number}: {quiz_question.text} (True/False) """)
        self.check_answer(quiz_answer=quiz_question.answer, user_answer=user_answer)

    def check_answer(self, quiz_answer, user_answer):
        # print('answer type', type(user_answer))
        # if user_answer != "True" or "False":
        #     print("you are wrong for answer!")
        #     print("please type True or False")
        #     self.question_number -= 1

        if quiz_answer.lower() == user_answer.lower():
            self.score += 1
            print('you are right!')
            print('next to the question')
        else:
            print("That's wrong.")
        print(f'Your current score is : {self.score}/{self.question_number}')
        print('\n')
    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     input(f"Q.{self.question_number} : {current_question.text}")

    def report_score(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.score}/{self.question_number}")
