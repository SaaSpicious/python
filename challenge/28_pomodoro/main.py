from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(time):
    count_down(time*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def enforce_double_digit(number):
    if number > 10:
        return number
    else:
        return f"0{number}"

def create_timer_text(count):
    minutes = enforce_double_digit(math.floor(count/60))
    seconds = enforce_double_digit(count % 60)
    timer_text = f"{minutes}:{seconds}"
    return timer_text

def count_down(count):
    canvas.itemconfig(timer_text,text=create_timer_text(count))
    window.after(1000,count_down,count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

title_label = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
title_label.grid(column=1,row=0)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text="",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",highlightthickness=0,command=start_timer(WORK_MIN))
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)

checkmarks = Label(text="✓",fg=GREEN,bg=YELLOW)
checkmarks.grid(column=1,row=3)

window.mainloop()