import words

chosen_word=words.get_word()
print(chosen_word)

lives=7

guess_list=[]
past_guesses=[]
for i in range(0,len(chosen_word)):
    guess_list.append("_")

while ("_" in guess_list and lives > 0):
    guess=input("Guess a letter! ").lower()
    if guess in past_guesses:
        print(f"You already guessed the letter {guess}")
    else:
        past_guesses += guess
        if chosen_word.count(guess) == 0:
            lives -= 6
            print(f"Letter not in the word, you have {lives} lives remaining.")
        else:
            for n in range(0,len(chosen_word)):
                if chosen_word[n] == guess:
                    guess_list[n] = guess
        print(guess_list)

if "_" not in guess_list:
    print("Congratulations, you have won!")
else:
    print("Sorry, you're dead...")