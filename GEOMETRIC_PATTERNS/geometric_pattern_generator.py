import turtle
import random

# --- Configuration ---
turtle.colormode(255) # Use 255 RGB values for colors
t = turtle.Turtle()
t.speed(0) # Fastest speed for drawing
t.hideturtle()

# --- Shape Functions ---

def draw_square(size, angle):
    """Draws a square and moves the turtle to a new position/angle."""
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.setheading(angle)
    t.pendown()
    t.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_triangle(size, angle):
    """Draws a triangle."""
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.setheading(angle)
    t.pendown()
    t.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

def draw_circle(radius):
    """Draws a circle."""
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    t.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# --- Main Logic ---
def generate_patterns(num_shapes=50):
    """Picks a random shape and draws it repeatedly."""
    shapes = [draw_square, draw_triangle, draw_circle]

    for _ in range(num_shapes):
        # 1. Randomly select a shape function
        shape_function = random.choice(shapes)
        
        # 2. Generate random parameters
        random_size = random.randint(20, 100)
        random_angle = random.randint(0, 360)
        
        # 3. Draw the shape
        if shape_function == draw_circle:
            shape_function(random_size) # Circle only needs radius
        else:
            shape_function(random_size, random_angle)
            
    t.screen.exitonclick() # Closes the window when clicked

if __name__ == "__main__":
    generate_patterns()