from turtle import Turtle, Screen
from extract_image import extract
import random
# import colorgram
# color_list = []
#
#
# def color_extractor(number_of_colors):
#     """Extracts set number of colors from a given image
#     and puts the rgb-tuples into a list."""
#     global color_list
#     number = 0
#     colors = colorgram.extract("image.jpg", number_of_colors)
#     for _ in range(number_of_colors):
#         tha_color = colors[number]
#         color_tuple = (tha_color.rgb.r, tha_color.rgb.g, tha_color.rgb.b)
#         color_list.append(color_tuple)
#         number += 1
#
#
# color_extractor(number_of_colors=30)
#
# print(color_list)


## TODO: 10 x 10; circle width = 20; space between circles = 50

tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()


x_coordinate = -300
y_coordinate = -300
tim.setpos(x_coordinate, y_coordinate)


for test in range(100):
    random_color = random.choice(extract)
    hex_color = '#%02x%02x%02x' % random_color
    if test == 10:
        y_coordinate = - 250
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 20:
        y_coordinate = - 200
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 30:
        y_coordinate = - 150
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 40:
        y_coordinate = - 100
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 50:
        y_coordinate = - 50
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 60:
        y_coordinate = 0
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 70:
        y_coordinate = 50
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 80:
        y_coordinate = 100
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 90:
        y_coordinate = 150
        x_coordinate = - 300
        tim.setpos(x_coordinate, y_coordinate)
    if test == 100:
        break
    tim.dot(20, hex_color)
    tim.forward(50)


screen = Screen()
screen.exitonclick()
