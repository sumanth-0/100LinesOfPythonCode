import turtle
import random
import colorsys

def setup_screen():
    """Setup turtle screen with black background"""
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title('Random Art Pattern Generator')
    screen.setup(width=800, height=800)
    return screen

def create_turtle():
    """Create and configure turtle object"""
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    turtle.colormode(255)
    return t

def get_random_color():
    """Generate a random RGB color"""
    hue = random.random()
    saturation = random.uniform(0.5, 1.0)
    value = random.uniform(0.5, 1.0)
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return tuple(int(c * 255) for c in rgb)

def draw_spiral_pattern(t, size, angle_increment):
    """Draw a spiral pattern with random colors"""
    for i in range(size):
        t.pencolor(get_random_color())
        t.forward(i * 2)
        t.right(angle_increment)

def draw_circular_pattern(t, radius, num_circles):
    """Draw concentric circles with random colors"""
    for i in range(num_circles):
        t.pencolor(get_random_color())
        t.circle(radius - i * (radius / num_circles))
        t.right(360 / num_circles)

def draw_star_pattern(t, size, num_points):
    """Draw star patterns with random colors"""
    angle = 180 - (180 / num_points)
    for i in range(num_points):
        t.pencolor(get_random_color())
        t.forward(size)
        t.right(angle)

def draw_fractal_tree(t, branch_len, angle, depth):
    """Draw a fractal tree pattern"""
    if depth > 0:
        t.pencolor(get_random_color())
        t.forward(branch_len)
        t.right(angle)
        draw_fractal_tree(t, branch_len * 0.7, angle, depth - 1)
        t.left(angle * 2)
        draw_fractal_tree(t, branch_len * 0.7, angle, depth - 1)
        t.right(angle)
        t.backward(branch_len)

def draw_random_polygons(t, num_polygons, max_size):
    """Draw random polygons at random positions"""
    for _ in range(num_polygons):
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()
        t.pencolor(get_random_color())
        sides = random.randint(3, 8)
        size = random.randint(20, max_size)
        for _ in range(sides):
            t.forward(size)
            t.right(360 / sides)

def main():
    """Main function to generate random art patterns"""
    screen = setup_screen()
    t = create_turtle()
    t.hideturtle()
    
    # Choose random pattern type
    patterns = ['spiral', 'circular', 'star', 'fractal', 'polygons']
    pattern_choice = random.choice(patterns)
    
    if pattern_choice == 'spiral':
        draw_spiral_pattern(t, 200, random.randint(60, 120))
    elif pattern_choice == 'circular':
        draw_circular_pattern(t, 200, random.randint(20, 50))
    elif pattern_choice == 'star':
        for _ in range(10):
            draw_star_pattern(t, random.randint(50, 150), random.randint(5, 12))
    elif pattern_choice == 'fractal':
        t.left(90)
        t.penup()
        t.goto(0, -200)
        t.pendown()
        draw_fractal_tree(t, 100, 30, 5)
    else:
        draw_random_polygons(t, 15, 80)
    
    screen.exitonclick()

if __name__ == '__main__':
    main()
