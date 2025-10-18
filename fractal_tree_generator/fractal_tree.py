import turtle
import random

def create_fractal_tree(t, branch_len, angle):
    """
    Recursively draws a fractal tree using turtle graphics
    
    Args:
        t: turtle object
        branch_len: length of the current branch
        angle: angle of branching
    """
    if branch_len < 5:  # Base case: stop when branches get too small
        return
    
    # Draw current branch
    t.forward(branch_len)
    
    # Save current position and angle
    pos = t.pos()
    heading = t.heading()
    
    # Right branch (make it slightly random for more natural look)
    t.right(angle + random.randint(-10, 10))
    create_fractal_tree(t, branch_len * 0.7, angle)
    
    # Go back to saved position and heading
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()
    
    # Left branch (make it slightly random for more natural look)
    t.left(angle + random.randint(-10, 10))
    create_fractal_tree(t, branch_len * 0.7, angle)
    
    # Return to start of current branch
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()

def main():
    # Setup screen and turtle
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title('Fractal Tree')
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.color('lime green')
    t.left(90)  # Point turtle upward
    t.penup()
    t.setpos(0, -200)  # Start at bottom of screen
    t.pendown()
    
    # Draw the tree
    create_fractal_tree(t, 100, 30)
    
    # Hide turtle and keep window open
    t.hideturtle()
    screen.mainloop()

if __name__ == '__main__':
    main()