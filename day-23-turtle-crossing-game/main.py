import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 600
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkeypress(player.go_up, "Up")
    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if it happens
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.has_finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()
        scoreboard.update_scoreboard()


screen.exitonclick()