from tkinter import *
from quiz_brain import *
THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=2, row=1)

        self.canvas_question = Canvas(width=300, height=250, highlightthickness=0, bg="#FFFFFF")
        self.question = self.canvas_question.create_text(
            150,
            125,
            width = 260,
            text="This is a question?!",
            font=("Arial", 16, "italic")
        )
        self.canvas_question.grid(column=1, row=2,columnspan=2,pady=50)

        pic_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=pic_true, highlightthickness=0,bg=THEME_COLOR,padx=20,pady=20,command=self.true_pressed)
        self.button_true.grid(column=1, row=3)

        pic_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=pic_false, highlightthickness=0,bg=THEME_COLOR,padx=20,pady=20,command=self.false_pressed)
        self.button_false.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_question.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas_question.itemconfig(self.question, text=q_text)
        else:
            self.canvas_question.itemconfig(self.question, text="You have reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas_question.config(bg="#00CC33")
        else:
            self.canvas_question.config(bg="#CC1111")
        self.window.after(1000,self.get_next_question)