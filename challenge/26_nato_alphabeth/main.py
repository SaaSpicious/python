import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

name = input("Which name do you need to have spelled? ").upper()

spelling = [alphabet[alphabet.letter == n].code.item() for n in name]

print(spelling)

