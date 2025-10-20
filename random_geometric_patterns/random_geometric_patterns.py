import turtle
import random

# inputs from user
moves = int(input("How many times should the cursor move? "))
sides = int(input("Enter the number of sides for the shape (e.g. 3 for triangle, 4 for square etc.): "))

# the drawing window
turtle.bgcolor("black")     # background color
turtle.speed(0)             # fastest drawing speed
turtle.pensize(2)           # line thickness
turtle.colormode(255)       # allows RGB color values

# function to return a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# draw repeated geometric pattern
for i in range(moves):
    turtle.color(random_color())     # choose a random color
    for j in range(sides):           # draw one polygon (according to no. of sides input by user)
        turtle.forward(100)
        turtle.right(360 / sides)
    
    # after each shape, rotate a little to make the spiral pattern
    turtle.right(360 / moves)

# finish up
turtle.hideturtle()
turtle.done()