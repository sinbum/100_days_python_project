class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        quiz_number = self.question_number + 1
        quiz_question = self.question_list[self.question_number]
        input(f"""Q.{quiz_number}: {quiz_question.text} (True/False) """)


    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     input(f"Q.{self.question_number} : {current_question.text}")


