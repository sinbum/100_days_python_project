from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)

quiz = QuizBrain(q_list=question_bank)
quiz.next_question()

