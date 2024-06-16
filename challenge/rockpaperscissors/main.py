import random
import hands

playerchoice=int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors!"))
computerchoice=random.randint(0,2)

print("Your choice")
print(hands.hands[playerchoice])
print("Computer's choice")
print(hands.hands[computerchoice])

if(computerchoice==playerchoice):
    print("It's a draw!")
elif computerchoice==0:
    if playerchoice==1:
        print("Player wins!")
    else:
        print("Computer wins!")
elif computerchoice==1:
    if playerchoice==0:
        print("Computer wins!")
    else:
        print("Player wins!")
elif computerchoice==2:
    if playerchoice==0:
        print("Player wins!")
    else:
        print("Computer wins!")