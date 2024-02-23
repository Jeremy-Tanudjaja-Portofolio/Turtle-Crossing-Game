from turtle import Turtle
import random as rand

class Car():

    car_list = []
    COLOR = ["blue","yellow","pink","purple","red","brown","black","orange"]
    move_speed = 1

    def __init__(self):
        for _ in range(0,1,1):
            self.car_list.append(self.create_car())

    def create_car(self):
        new_length = rand.randint(1,3)
        new_y = rand.randint(-200,200)
        car = Turtle()
        car.shape("square")
        car.color(rand.choice(self.COLOR))
        car.penup()
        car.turtlesize(stretch_wid= 1, stretch_len=new_length)
        car.goto(x = 380, y = new_y )
        car.setheading(180)
        return car

    def move_car(self):
        for car in self.car_list:
            car.forward(20)

    def add_speed(self):
        self.move_speed = self.move_speed + 1
        for car in self.car_list:
            car.speed(self.move_speed)

    def detect_collision_wall(self):
        for car in self.car_list:
            if car.xcor() < -400:
                del car

    def detect_collision_player(self,player):
        for car in self.car_list:
            if player.distance(car)<5:
                print("collide")
                return False
