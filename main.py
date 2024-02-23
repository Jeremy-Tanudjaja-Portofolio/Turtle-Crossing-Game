from turtle import Screen
from player import Player
from cars import Car
from level import Level
import time

game_is_on = True

screen = Screen()
screen.setup(width= 800, height=600)
screen.listen()
screen.tracer(0)

level = Level()

player= Player()
player.reset_position()

screen.onkeypress(fun = player.go_up, key="Up")
screen.onkeypress(fun = player.go_down, key = "Down")
screen.onkeypress(fun = player.go_left, key="Left")
screen.onkeypress(fun = player.go_right, key = "Right")

level.write_level()

while game_is_on:
    time.sleep(0.2)
    cars = Car()
    screen.update()
    cars.move_car()
    cars.detect_collision_wall()
    if cars.detect_collision_player(player)==False:
        level.lose_level()
        time.sleep(5)
        game_is_on = False
    if level.player_next_level(player):
        level.increase_level()
        level.write_level()
        cars.add_speed()
        player.reset_position()