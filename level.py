from turtle import Turtle

class Level(Turtle):

    level = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-385, 270)
        self.pendown()

    def increase_level(self):
        self.level = self.level + 1

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}",font=("Verdana", 18, "normal"))

    def lose_level(self):
        self.penup()
        self.goto(-40, 0)
        self.pendown()
        self.write("GAME OVER", font=("Verdana", 26, "normal"))

    def player_next_level(self,player):
        if player.ycor()>290:
            self.increase_level()
            self.write_level()
            return True