import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(80)
t.colormode(255)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def draw_spirograph(size_of_gap):
    for angle in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())


draw_spirograph(5)






screen = Screen()
screen.exitonclick()