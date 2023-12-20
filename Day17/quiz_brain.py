class QuizBrain():

    def __init__(self, q_list):
        self.questions_list = q_list
        self.number = 0
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.questions_list)

    
    def next_question(self):
        current_question = self.questions_list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You've got it right! ")
            
        else:
            print("That's wrong. ")
            print(f"The correct answer would be: {correct_answer}")
        print(f"The correct answer would be: {correct_answer}")
        print(f"Your current score is {self.score} / {self.number}")
        print("\n")

  
