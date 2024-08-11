from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(15)
        self.hideturtle()
        self.color("white")
        self.font = "Courier"
        self.font_size = 40
        self.draw_center()


    def refresh(self,points):
        self.clear()
        self.goto(-50,460)
        self.write(arg=points[0],move=False, font=(self.font, self.font_size, 'bold'))
        self.goto(50, 460)
        self.write(arg=points[1],move=False, font=(self.font, self.font_size, 'bold'))
        self.draw_center()

    def draw_center(self):
        for i in range(1,11):
            position = 340-((i-1)*90)
            self.penup()
            self.goto(0,position)
            self.pendown()
            self.goto(0, position + 45)
            self.penup()