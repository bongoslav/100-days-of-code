from turtle import Turtle, Screen
import random
import turtle as t

# import colorgram
# colors = colorgram.extract('image.jpg', 6)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_lists = [(245, 3, 245), (246, 5, 246), (42, 202, 202), (69, 240, 111), (69, 236, 222), (149, 149, 15)]


tim = Turtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.setposition(-250, -250)
tim.ht()

for rows in range(10):
    for columns in range(10):
        tim.setx(tim.xcor() + 50)
        tim.dot(20, random.choice(color_lists))
    tim.setx(tim.xcor() - 10 * 50)
    tim.sety(tim.ycor() + 50)


screen = Screen()
screen.exitonclick()