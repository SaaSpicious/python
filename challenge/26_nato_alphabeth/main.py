import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

def get_phonetic():
    name = input("Which name do you need to have spelled? ").upper()
    try:
        spelling = [alphabet[alphabet.letter == n].code.item() for n in name]
    except ValueError:
        print("Sorry, only letters allowed in here!")
        get_phonetic()
    else:
        print(spelling)

get_phonetic()