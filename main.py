import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
carmanager = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.update()
    for car in carmanager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.reset()
        carmanager.up_the_speed()
        scoreboard.increase_level()

screen.exitonclick()
