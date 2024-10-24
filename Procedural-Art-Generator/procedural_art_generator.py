import turtle
import random

# Function to draw a random dot pattern
def draw_random_pattern(turtle_obj, num_shapes):
    for _ in range(num_shapes):
        # Randomize position
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        
        # Set random color
        turtle_obj.color(random.random(), random.random(), random.random())
        
        # Draw a random shape (circle, square, or triangle)
        shape_choice = random.choice(['circle', 'square', 'triangle'])
        
        if shape_choice == 'circle':
            radius = random.randint(10, 100)
            turtle_obj.circle(radius)
        elif shape_choice == 'square':
            side_length = random.randint(20, 100)
            for _ in range(4):
                turtle_obj.forward(side_length)
                turtle_obj.right(90)
        elif shape_choice == 'triangle':
            side_length = random.randint(20, 100)
            for _ in range(3):
                turtle_obj.forward(side_length)
                turtle_obj.right(120)

def main():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle object
    art_turtle = turtle.Turtle()
    art_turtle.speed(0)  # Fastest drawing speed

    # Draw a random pattern
    draw_random_pattern(art_turtle, num_shapes=50)  # Change this number for more or fewer shapes

    # Hide the turtle and finish
    art_turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
