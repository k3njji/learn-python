# asking the questions
# checking if the answe was correct
# checking if we are at the end of the quiz

# attributes
# question_number = 0
# questions_list

# methods next_question()

class BrainQuestion:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def check_answer(self, ans):
        if(ans == self.questions[self.question_number].answer):
            print("Congrats! You got it right!")
            return True
        else:
             print("Sorry, the correct answer is", self.questions[self.question_number].answer)

    def current_score(self):
         print(f"Your current score is: {self.score}/{len(self.questions)}")
        
    def still_question(self):
        return self.question_number < len(self.questions)
    
    def add_score(self, ans):
        if(self.check_answer(ans)):
            self.score+=1

    def next_question(self):
            current_question = self.questions[self.question_number]
            self.add_score(input(f"Q.{self.question_number+1}: {current_question.question} (True/False): "))
            self.question_number+=1  
