class Question:

    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

    def check_answer(self,answer):
        if self.answer.lower() == answer.lower():
            print("The answer was correct!")
            return True
        else:
            print("That's wrong!")
            return False