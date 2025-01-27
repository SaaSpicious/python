import datetime as dt
import random

def create_list_from_file(filename):
    file = open(filename,"r")
    return file.readlines()


def pick_random_quote(quote_list):
    return random.choice(quote_list)

print(dt.datetime.now().weekday())

quote_list = create_list_from_file("quotes.txt")
print(pick_random_quote(quote_list))