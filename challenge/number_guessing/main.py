import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_guess(choice, solution,turns):
    """Checks if the answer is correct and returns the new number of turns"""
    if choice>solution:
        print("Your number is too high!")
    elif choice < solution:
        print("Your number is too low!")
    else:
        return turns

    print(f"You have {turns} turns remaining.")
    return turns-1

def set_difficulty():
    difficulty = ""
    while difficulty not in ("easy", "hard"):
        difficulty = input("Please choose your difficulty. (easy/hard) ")

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print("Welcome to the number guessing game.")

turns = set_difficulty()

print("I'm thinking of a number between 1 - 100.")
print(f"You have {turns} turns to guess my number.")
choice=0
solution=random.randint(1,100)

while choice != solution and turns>0:
    choice=int(input("Please guess a number! "))
    turns=check_guess(choice,solution,turns)

if choice == solution:
    print(f"Congratulations, you have guessed the right number {solution}")
else:
    print(f"Oh no, you ran out of turns. The right number was {solution}.")