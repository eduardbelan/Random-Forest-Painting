# from turtle import Turtle, Screen
# from extract_image import extract
# import random
# import colorgram
# color_list = []
#
#
# Color Extractor from image
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

# tim = Turtle()
# tim.speed(0)
# tim.penup()
# tim.hideturtle()


# Turtle - Random Walk: my_Version

# tim.width(10)
# for _ in range(200):
#     random_color = random.choice(extract)
#     hex_color = '#%02x%02x%02x' % random_color
#     f_b = random.randint(1, 101)
#     r_l = random.randint(1, 101)
#     if f_b <= 50:
#         tim.pencolor(hex_color)
#         tim.forward(20)
#     else:
#         tim.pencolor(hex_color)
#         tim.back(50)
#     if r_l <= 50:
#         tim.pencolor(hex_color)
#         tim.right(50)
#     else:
#         tim.pencolor(hex_color)
#         tim.left(90)


# Turtle - Random Walk: my_other_Version

# directions = [0, 90, 180, 270]
# for _ in range(200):
#     # r = random.randint(1, 255)
#     # g = random.randint(1, 255)
#     # b = random.randint(1, 255)
#     # random_color = (r, g, b)
#     random_color = random.choice(extract)
#     hex_color = '#%02x%02x%02x' % random_color
#     tim.width(5)
#     tim.pencolor(hex_color)
#     tim.forward(50)
#     tim.setheading(random.choice(directions))


# # Hirst 'Dot' Painting
# x_coordinate = -300
# y_coordinate = -300
# tim.setpos(x_coordinate, y_coordinate)
#
# for test in range(100):
#     random_color = random.choice(extract)
#     hex_color = '#%02x%02x%02x' % random_color
#     if test == 10:
#         y_coordinate = - 250
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 20:
#         y_coordinate = - 200
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 30:
#         y_coordinate = - 150
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 40:
#         y_coordinate = - 100
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 50:
#         y_coordinate = - 50
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 60:
#         y_coordinate = 0
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 70:
#         y_coordinate = 50
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 80:
#         y_coordinate = 100
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 90:
#         y_coordinate = 150
#         x_coordinate = - 300
#         tim.setpos(x_coordinate, y_coordinate)
#     if test == 100:
#         break
#     tim.dot(30, hex_color)
#     tim.forward(50)
#
#
# screen = Screen()
# screen.exitonclick()
