# What is a Tuple?
# - A Tuple is a Datatype
# - Syntax: (1, 3, 8)
# - round brackets, entries are separated by a comma
# - Tuples ara "Immutable", the values can not be changed
# Why using a Tuple?
# - If you have Data that you want to stay the same as a constant
# What if I need to change Data in the Tuple?
# - put it in a list: list(my_Tuple) and change it then


# Importing Modules, Installing Packages, Working with Aliases

# Different Options:

# if you use a module only a view times this method of importing is recommended:
# import turtle
# tim = turtle.Turtle()

# if you use a module often in your code this method is recommended:
# from turtle import Turtle
# tim = Turtle()

# from turtle import *
# - imports everything from that module
# - is not recommended because when you use attributes and methods later
#   in your file it can get confusing


# Aliasing Modules
# Modules can be given a new Name when u import them

# import turtle as t
# tim = t.Turtle()


# Installing Modules
# Python has a standard Library to get you started:
# - some modules are already within that standard library
# - the turtle module is part of the python standard library

# What if the module you need is not part of the standard library?
# You have to install the module:
# - look for the module you need on "pypi.org"
# - import the module "import heroes"
# - you get a warning that the module is not yet installed
# - follow the prompt to install the module
# - done


# Turtle - 10 shapes: Triangle to Decagon
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# Turtle - Random Walk: my_Version
# for _ in range(100):
#     f_b = random.randint(1, 101)
#     r_l = random.randint(1, 101)
#     if f_b <= 50:
#         tim.color(random.choice(colours))
#         tim.forward(20)
#     else:
#         tim.color(random.choice(colours))
#         tim.back(20)
#     if r_l <= 50:
#         tim.color(random.choice(colours))
#         tim.right(90)
#     else:
#         tim.color(random.choice(colours))
#         tim.left(90)


# Turtle - Random Walk: other_Version
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(20)
#     tim.setheading(random.choice(directions))


# Turtle - Drawing Circles: my_Version
# instance = 0
# for degree in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(instance)
#     instance += 3.6

# Turtle - Drawing Circles: other_Version
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(10)
