from tkinter import *
from tkinter import messagebox

import pandas
from pandas import *
import random

try:
    word_map = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_map = pandas.read_csv("data/french_words.csv")

word_dict = word_map.to_dict(orient="records")


BACKGROUND_COLOR = "#B1DDC6"
word_pair = {}

def next_card():
    global word_dict, word_pair
    canvas_card.itemconfig(card_image,image=card_front)
    canvas_card.itemconfig(card_language, text="French", font=("Arial", 40, "italic"),fill="black")
    canvas_card.itemconfig(card_word, text="Example", font=("Arial", 60, "bold"),fill="black")
    word_pair=random.choice(word_dict)
    canvas_card.itemconfig(card_word,text=word_pair["French"])
    count_down(5)


def count_down(timer):
    global word_pair
    if timer > 0:
        window.after(1000,count_down,timer - 1)
        canvas_card.itemconfig(countdown,text=str(timer))
    else:
        canvas_card.itemconfig(countdown, text="0")
        flip_card(word_pair)

def flip_card(word_pair):
    canvas_card.itemconfig(card_image,image=card_back)
    canvas_card.itemconfig(card_language, text="English",font=("Arial",40,"italic"),fill="white")
    canvas_card.itemconfig(card_word, text=word_pair["English"],font=("Arial", 60, "bold"),fill="white")

def remove_word():
    global word_dict,word_pair
    word_dict.remove(word_pair)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv")
    word_map = pandas.read_csv("data/words_to_learn.csv")
    word_dict = word_map.to_dict(orient="records")
    next_card()


window = Tk()
window.title("Flip Card Program")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

canvas_card = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas_card.create_image(400,270,image=card_front)
card_language = canvas_card.create_text(400,150,text="French",font=("Arial",40,"italic"))
card_word = canvas_card.create_text(400,263,text="Example",font=("Arial",60,"bold"))
countdown = canvas_card.create_text(720,60,text="5",font=("Arial",30,"bold"))
canvas_card.grid(column=1, row=1,columnspan=2)


pic_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=pic_wrong,highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=2)

pic_right = PhotoImage(file="images/right.png")
button_right = Button(image=pic_right,highlightthickness=0, command=remove_word)
button_right.grid(column=2, row=2)

next_card()

window.mainloop()