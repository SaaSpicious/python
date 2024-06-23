import art
import deck

start_round="y"
while start_round=="y":
    print(art.logo)

    player_cards=[]
    bank_cards=[]

    for i in range(0,2):
        player_cards.append(deck.draw_card())
        bank_cards.append(deck.draw_card())

    print(f"Your cards are {player_cards}")
    print(f"The bank's first card is: {bank_cards[0]}")

    action=input("Do you want to draw a card? (y/n) ")
    while action=="y":
        player_cards.append(deck.draw_card())
        if sum(player_cards) >= 21:
           player_cards=deck.shrink_aces(player_cards)
        print(f"Your cards are {player_cards}")
        if sum(player_cards) <= 21:
            action = input("Do you want to draw another card? (y/n) ")
        else:
            action = "n"

    if sum(player_cards)>21:
        print("Sorry, you busted and lost!")
    else:
        while sum(bank_cards)<17:
            bank_cards.append(deck.draw_card())
            if sum(bank_cards) > 21:
                bank_cards = deck.shrink_aces(bank_cards)
        print(f"The bank finished with a hand of {bank_cards}.")

        if sum(bank_cards) > 21:
            print("The bank busted, you won!")
        elif sum(bank_cards) > sum(player_cards):
            print("Sorry, you lost against the bank's hand!")
        elif sum(bank_cards) == sum(player_cards):
            print("It's a draw!")
        else:
            print("Great, you won!")

    start_round=input("Would you like to play another round? (y/n) ")

print("Thanks for playing Blackjack with me.")