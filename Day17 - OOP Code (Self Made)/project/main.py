from question_model import Question
from data import question_data
from quiz_brain import BrainQuestion

questions = []
for data in question_data:
    questions.append(Question(data['text'], data['answer']))

quiz = BrainQuestion(questions)

while(quiz.still_question()):
    # print("Your current score: ", quiz.score)
    quiz.next_question()
    quiz.current_score()
