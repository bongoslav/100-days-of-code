from turtle import Turtle
import random


class Food(Turtle):  # inheritance -> So my food class is sort of like a Turtle

    def __init__(self):
        super().__init__()  # inherit the init from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # creating a 10x10 circle
        self.color("green")
        self.speed("fastest")
        self.refresh()  # we add the method so that the refresh method is called whenever the Food class is called

    def refresh(self):
        random_x = random.randrange(-180, 180, 20)  # step = 20 -> always generates the food in the middle of the snake
        random_y = random.randrange(-180, 180, 20)
        self.goto(random_x, random_y)