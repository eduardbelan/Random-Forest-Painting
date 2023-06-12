# Functions as Inputs
#
# When you use a function as an argument inside another function,
# and that argument should only be triggered when a certain key is pressed,
# you have to leave the parentheses out:
# Syntax:
#
# def my_function():
#     do this
#
# screen.onkey(key="space", fun=my_function)
#
# Now it will trigger the function only when the spacebar is pressed,
# IMPORTANT: when you add the parentheses into the argument as well, the function will be called,
#            no matter if the spacebar is pressed or not


# Syntax:
#
# def function_a(something):
#     do this with something
#     then do this
#     finally do this
#
# def function_b():
#     do this
#
# function_a(function_b)


# Higher Order Function

# A Higher Order Function is a function, that is taking another function as an input.
# And then the Higher Order Function is working within itself with the other function as an input.


# General Tips & Tricks:
# when using methods that you didn't create yourself:
#   use Keyword Arguments instead of Positional Arguments
#
# def my_function(a, b, c):
#     do this with a
#     then do this with b
#     finally do this with c
#
# Keyword Arguments:
# my_function(a=1, b=2, c=3)
#
# Positional Arguments:
# my_function(1, 2, 3)


# More Objects out of the same Class:
# we are making Objects (turtles) out of the same class, Turtle()
# the different turtles are also called "Instances"
# They are examples of the Turtle-Object
# They can have different attributes like different colors and can perform different methods at the same time

# When talking about what each instance is doing at a given time, we call it the "State" of the Instance
# the state of turtle_a is green, the state of turtle_b is yellow
