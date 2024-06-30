import art
import gamedata
import os

def evaluate_guess(first_choice,second_choice,guess):
    if first_choice["follower_count"] < second_choice["follower_count"]:
        return guess == "higher"
    else:
        return guess == "lower"

def format_data(data):
    return f"{data["name"]}, a {data["description"]} from {data["country"]}"

points=0
correct = True

first_choice=gamedata.get_entry()
second_choice=first_choice

while correct:
    clear = lambda: os.system('cls')
    clear()
    print(art.logo)
    if points > 0:
        print(f"You currently have {points} correct guesses")

    while second_choice == first_choice:
        second_choice=gamedata.get_entry()

    print("Now lets compare:")
    print(format_data(first_choice))
    print(art.vs)
    print(format_data(second_choice))

    guess = ""
    while guess not in ("higher","lower"):
        guess = input("What do you think, higher or lower? ")

    correct = evaluate_guess(first_choice,second_choice,guess)
    if correct:
        points+=1
        first_choice=second_choice

print(f"Sorry, wrong guess! {first_choice["name"]} has {first_choice["follower_count"]} followers, while {second_choice["name"]} has {second_choice["follower_count"]} followers")