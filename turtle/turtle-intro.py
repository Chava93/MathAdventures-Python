from turtle import *

# Basic Functions
# shape("turtle") give a shape to our object
# forward() or fd(), right() or rt(), left() or lt()
# Move without drawing – penup(), pendown()
def square(side_length = 100):
    """
    Draw a square with my turtle
    Input
    -----
        side_length: default = 100
            lenght of each side of the square
    """
    for side in range(4):
        fd(side_length)
        rt(90)

def circleOfSquares(n_squares=60, side_square_length=100, sep_degrees=5):
    # try circleOfSquares(80)
    for s in range(n_squares):
        square(side_square_length)
        rt(sep_degrees)

def triangle_equilateral(side_length=100):
    for side in range(3):
        fd(side_length)
        rt(120)

def polygon(n_sides=5, side_length=100):
    interior = 180*(n_sides-2)
    for side in range(n_sides):
        fd(side_length)
        rt(180-interior/n_sides)

def squareSpiral(n_squares=60, sep_degrees=5, init_length=5, increment_length=5):
    """
    Create n_squares incrementing each square side length by increment_length and
    rotating sep_degrees between each square.
    """
    for s in range(n_squares):
        square(init_length + increment_length*s)
        rt(sep_degrees)

def star(side_length=100):
    """
    A star has 5 sides of the same init_length
    thus, 180/5 = 36 degrees (of internal angle)
    then 180-36 = 144 (of external anlge)
    """
    for side in range(5):
        fd(side_length)
        rt(144)

def starSpiral(n_stars=60, sep_degrees=5, init_length=5, increment_length=5):
    for s in range(n_stars):
        star(init_length + increment_length*s)
        rt(sep_degrees)

from random import randint
def wander():
    "p.62 Math Advd."
    while True:
        fd(3)
        if abs(xcor()) >= 200 or abs(ycor()) >= 200:
            lt(randint(90,180))

if __name__=="__main__":
    shape("turtle")
    speed(0) #0 fastest - 1 slowest
    wander()
