from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.font = "Courier"
        self.font_size = 30
        self.goto(0,260)

    def refresh(self,level):
        self.clear()
        self.write(f"Level: {level}", move=False, align="center",font=(self.font, self.font_size, 'bold'))

    def game_over(self):
        self.goto (0,0)
        self.font_size = 40
        self.write("GAME OVER!", move=False, align="center",font=(self.font, self.font_size, 'bold'))