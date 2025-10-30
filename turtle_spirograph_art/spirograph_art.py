import turtle
import random

# --- 1. Setup the Screen and Turtle ---
try:
    # Create a screen for the art
    screen = turtle.Screen()
    screen.bgcolor("black") # Set a black background
    screen.title("Spirograph Art Generator")

    # Create a turtle to do the drawing
    t = turtle.Turtle()
    t.speed(0) # '0' is the fastest speed
    t.hideturtle() # Hide the arrow cursor
    t.width(2) # Make the lines a bit thicker

    # --- 2. Define the Color Palette ---
    # A list of bright colors to choose from
    colors = [
        "red", "orange", "yellow", "green", "blue", 
        "cyan", "purple", "magenta", "white"
    ]

    # --- 3. The Drawing Loop ---
    # This loop will draw 36 overlapping circles
    num_circles = 36
    radius = 120 # The size of each circle

    for _ in range(num_circles):
        # Pick a new random color for each circle
        t.color(random.choice(colors))
        
        # Draw one circle
        t.circle(radius)
        
        # Tilt the turtle's "pen" by 10 degrees
        # (360 degrees / 36 circles = 10 degrees)
        t.left(10)

    # --- 4. Finish ---
    print("Art generation complete! Click the window to close.")
    # This keeps the window open until you click on it
    screen.exitonclick()

except turtle.Terminator:
    # This catches the error if the user closes the window early
    print("Drawing terminated.")
except Exception as e:
    print(f"An error occurred: {e}")