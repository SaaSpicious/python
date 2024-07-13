from question import Question
import data

class Prompter:

    def __init__(self):
        self.question_folder=self.load_questions()
        self.question_count = 0
        self.correct_count = 0


    def load_questions(self):
        question_folder=[]
        for n in data.question_data:
            question = Question(n["text"],n["answer"])
            question_folder.append(question)
        return question_folder