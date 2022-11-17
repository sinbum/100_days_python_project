from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data['question'], data['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(q_list=question_bank)


while quiz.still_has_question():
    quiz.next_question()

quiz.report_score()