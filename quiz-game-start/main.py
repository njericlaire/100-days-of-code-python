from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
print(question_data)
for i in question_data:
    text=i["question"]
    answer=i["correct_answer"]
    new_question=Question(text,answer)
    question_bank.append(new_question)
Quiz=QuizBrain(question_bank)


while Quiz.still_has_question():
    Quiz.nextQuestion()

print("You have completed the quiz")
print(F"You total score is {Quiz.score}/{Quiz.question_number}")


       
