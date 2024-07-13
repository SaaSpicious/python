from prompter import Prompter
import random

print("Welcome to the Quiz App!")

prompter = Prompter()

while prompter.question_count < 5:
    prompter.question_count += 1
    print(f"===== Here's question number {prompter.question_count} =====")
    randomize = random.randint(0,len(prompter.question_folder)-1)
    question = prompter.question_folder[randomize]
    prompter.question_folder.pop(randomize)
    response = input(f"{question.text} (True/False) ")
    if question.check_answer(response):
        prompter.correct_count += 1
    print(f"You've got {prompter.correct_count}/{prompter.question_count} right!")