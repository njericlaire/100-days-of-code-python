class QuizBrain:
    def __init__(self,quiz_list):
        self.question_number=0
        self.quiz_list=quiz_list
        self.score=0
    
    def nextQuestion(self):
        question=self.quiz_list[self.question_number]
        self.question_number+=1
        player_answer=input(f"Q {self.question_number}: {question.text} True/False ")
        self.check_anwer(player_answer,question.answer)

    def still_has_question(self):
        if self.question_number<len(self.quiz_list):
            return True
        else:
            return False  
    
    def check_anwer(self,current_answer,correct_answer):
        if current_answer.lower()==correct_answer.lower():
            print("That was the correct answer")
            self.score+=1
            
        else:
            print(f"You got it wrong the correct answer is {correct_answer}")
        print(f"Your score is score {self.score}/{self.question_number}")
        print("\n")