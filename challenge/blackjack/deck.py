import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """Returns a random card from the deck"""
    return random.choice(cards)

def shrink_aces(hand):
    """Checks for aces in a hand and replaces the first instance with a 1"""
    for n in range(0, len(hand)):
        if hand[n] == 11:
            hand[n] = 1
            return hand
    return hand