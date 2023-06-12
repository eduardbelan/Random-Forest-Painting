from turtle import Turtle, Screen
from extract_image import extract
import random
from PIL import Image
import os


FILE = "image.ps"


def save_painting(screen):
    """
    Save your random walk painting as a png file.
    (GhostScript is required and must be accessible, must be added to global path variables)
    In this case we're saving it as a .png file
      - can be set to other file type if needed, adjustments may be necessary
    """

    # save random walk as PostScript file
    canvas = screen.getcanvas()
    canvas.postscript(file=FILE)

    # convert PostScript file to PNG
    image = Image.open(FILE)
    png_filename = "random-walk-painting.png"
    image.save(png_filename)


def wrap_turtle(tim, screen_width, screen_height):
    """
    line reappears at the opposite side of the screen
    """
    x, y = tim.position()
    if x > screen_width / 2:
        tim.penup()
        tim.goto(-screen_width / 2, y)
        tim.pendown()
    elif x < -screen_width / 2:
        tim.penup()
        tim.goto(screen_width / 2, y)
        tim.pendown()
    elif y > screen_height / 2:
        tim.penup()
        tim.goto(x, -screen_height / 2)
        tim.pendown()
    elif y < -screen_height / 2:
        tim.penup()
        tim.goto(x, screen_height / 2)
        tim.pendown()


def hirst_painting():
    """
    Hirst 'Dot' Painting, larger image Version
    """

    # turtle settings
    tim = Turtle()
    tim.speed(0)
    tim.penup()
    tim.hideturtle()
    x_coordinate = -540
    y_coordinate = -540
    tim.setpos(x_coordinate, y_coordinate)

    # screen setup
    screen = Screen()
    screen.setup(1200, 1200)

    # dot coordinates
    for test in range(100):
        random_color = random.choice(extract)
        hex_color = '#%02x%02x%02x' % random_color
        if test == 10:
            y_coordinate = - 420
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 20:
            y_coordinate = - 300
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 30:
            y_coordinate = - 180
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 40:
            y_coordinate = - 60
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 50:
            y_coordinate = 60
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 60:
            y_coordinate = 180
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 70:
            y_coordinate = 300
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 80:
            y_coordinate = 420
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 90:
            y_coordinate = 540
            x_coordinate = - 540
            tim.setpos(x_coordinate, y_coordinate)
        if test == 100:
            break
        tim.dot(75, hex_color)
        tim.forward(120)

    # save image
    #   - activate os.remove(FILE) after function call to delete PostScript file automatically
    #   - or leave deactivated and delete the PostScript file manually
    save_painting(screen)

    # exit when finished
    screen.exitonclick()


# def hirst_painting():
#     """
#     Hirst 'Dot' Painting, smaller image Version
#     """
#
#     # turtle settings
#     tim = Turtle()
#     tim.speed(0)
#     tim.penup()
#     tim.hideturtle()
#     x_coordinate = -360
#     y_coordinate = -360
#     tim.setpos(x_coordinate, y_coordinate)
#
#     # screen setup
#     screen = Screen()
#     screen.setup(800, 800)
#
#     # dot coordinates
#     for test in range(100):
#         random_color = random.choice(extract)
#         hex_color = '#%02x%02x%02x' % random_color
#         if test == 10:
#             y_coordinate = - 280
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 20:
#             y_coordinate = - 200
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 30:
#             y_coordinate = - 120
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 40:
#             y_coordinate = - 40
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 50:
#             y_coordinate = 40
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 60:
#             y_coordinate = 120
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 70:
#             y_coordinate = 200
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 80:
#             y_coordinate = 280
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 90:
#             y_coordinate = 360
#             x_coordinate = - 360
#             tim.setpos(x_coordinate, y_coordinate)
#         if test == 100:
#             break
#         tim.dot(50, hex_color)
#         tim.forward(80)
#
#     # save image
#     #   - activate os.remove(FILE) after function call to delete PostScript file automatically
#     #   - or leave deactivated and delete the PostScript file manually
#     save_painting(screen)
#
#     # exit when finished
#     screen.exitonclick()


def random_walk_diagonal(line_width, speed, screen_width, screen_height, walk_range,
                         ahead_length, back_length, right_angle, left_angle):
    """
    Random Forest Walk with diagonal lines.
    Set Parameters:
    - dot width
    - speed
    - screen height
    - screen width
    - range of walk
    - forward movement length
    - backward movement length
    - right angle
    - left angle
    """

    # turtle settings
    tim = Turtle()
    tim.speed(speed)
    # tim.penup()
    tim.hideturtle()
    tim.width(line_width)

    # screen setup
    screen = Screen()
    screen.setup(screen_width, screen_height)
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    # loop to generate random walk with
    #   - set range
    #   - set angles (right/left)
    #   - set walk distance (forward/back)
    for _ in range(walk_range):
        random_color = random.choice(extract)
        hex_color = '#%02x%02x%02x' % random_color
        f_b = random.randint(1, 101)
        r_l = random.randint(1, 101)
        if f_b <= 50:
            tim.pencolor(hex_color)
            tim.forward(ahead_length)
        else:
            tim.pencolor(hex_color)
            tim.back(back_length)

        if r_l <= 50:
            tim.pencolor(hex_color)
            tim.right(right_angle)
        else:
            tim.pencolor(hex_color)
            tim.left(left_angle)

        # call wrap_turtle for random walk to appear on opposite side if it disappears on one side
        wrap_turtle(tim, screen_width, screen_height)

    # save image
    #   - activate os.remove(FILE) after function call to delete PostScript file automatically
    #   - or leave deactivated and delete the PostScript file manually
    save_painting(screen)

    # exit screen after random walk is finished
    screen.exitonclick()


def random_walk_squares(line_width, speed, screen_width, screen_height, walk_range, ahead_length):
    """
    Random Walk with horizontal and vertical lines.
    Set Parameters:
    - dot width
    - speed
    - screen height
    - screen width
    - range of walk
    - forward movement length
    """

    # turtle settings
    tim = Turtle()
    tim.speed(speed)
    # tim.penup()
    tim.hideturtle()
    tim.width(line_width)

    # screen setup
    screen = Screen()
    screen.setup(screen_width, screen_height)
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    # generate random walk with
    #   - set directions (right, left, up, down)
    #   - set length
    #   - allowed to walk back on same path (can be changed)
    #   - random color values possible but not used
    #       - can be integrated into random_walk_diagonal() as well
    directions = [0, 90, 180, 270]
    for _ in range(walk_range):
        # r = random.randint(1, 255)
        # g = random.randint(1, 255)
        # b = random.randint(1, 255)
        # random_color = (r, g, b)
        random_color = random.choice(extract)
        hex_color = '#%02x%02x%02x' % random_color
        tim.pencolor(hex_color)
        tim.forward(ahead_length)
        tim.setheading(random.choice(directions))
        wrap_turtle(tim, screen_width, screen_height)

    # save image
    #   - activate os.remove(FILE) after function call to delete PostScript file automatically
    #   - or leave deactivated and delete the PostScript file manually
    save_painting(screen)

    # exit screen after random walk is finished
    screen.exitonclick()


# Hirst Dot Painting
# hirst_painting()


# Random Forest Painting - Diagonal Lines
# random_walk_diagonal(line_width=10, speed=0, screen_width=1500, screen_height=1500, walk_range=200,
#                      ahead_length=100, back_length=100, right_angle=90, left_angle=50)


# Random Forest Painting - Squares
# random_walk_squares(line_width=10, speed=0, screen_width=1500, screen_height=1500, walk_range=400, ahead_length=100)


# activate only, when save_painting() is active in function
#   - save_painting() is active in every function, deactivate if needed
os.remove(FILE)
