def replace_name(base_letter, name):
    finished_letter = base_letter.replace("[name]", name)
    return finished_letter


def store_letter(letter,name):
    with open("./Output/ReadyToSend/" + name, "w") as target_letter:
        target_letter.write(letter)


with open("./Input/Letters/starting_letter.txt") as base_letter_file:
    base_letter = base_letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    store_letter(replace_name(base_letter,name.strip()),name.strip())