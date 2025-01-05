from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text,text=create_timer_text(25*60))
    title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    global timer
    global reps
    timer = False
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer
    reps   += 1
    timer = True

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    count_down(work_sec)
    title_label = Label(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label = Label(text="BREAK", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label = Label(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    else:
        count_down(work_sec)
        title_label = Label(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))


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
    global timer
    if count > 0 and timer:
        window.after(1000,count_down,count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

title_label.grid(column=1,row=0)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text="",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

checkmarks = Label(text="✓",fg=GREEN,bg=YELLOW)
checkmarks.grid(column=1,row=3)

window.mainloop()