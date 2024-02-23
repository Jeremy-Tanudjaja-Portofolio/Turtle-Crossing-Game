from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)

    def reset_position(self):
        self.goto(x = 0, y = -280)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)

    def go_left(self):
        self.setheading(180)
        self.forward(20)
        self.setheading(90)

    def go_right(self):
        self.setheading(0)
        self.forward(20)
        self.setheading(90)