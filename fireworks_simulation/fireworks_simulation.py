import turtle
import random
import math

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Fireworks Show")
screen.tracer(0)

artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)
artist.penup()

particles_x = []
particles_y = []
particles_vx = []
particles_vy = []
particles_color = []
particles_life = []

rockets_x = []
rockets_y = []
rockets_vy = []
rockets_color = []

def launch_burst(x, y, main_color):
    for _ in range(random.randint(40, 80)):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        color = main_color if random.random() > 0.7 else 'white'
        particles_x.append(x)
        particles_y.append(y)
        particles_vx.append(vx)
        particles_vy.append(vy)
        particles_color.append(color)
        particles_life.append(1.0)

try:
    while True:
        if random.random() < 0.03:
            rockets_x.append(random.randint(-380, 380))
            rockets_y.append(-290)
            rockets_vy.append(random.uniform(13, 16))
            rockets_color.append(random.choice(['red', 'yellow', 'cyan', 'magenta', 'lime', 'orange']))

        artist.clear()

        for i in range(len(rockets_x) - 1, -1, -1):
            rockets_vy[i] -= 0.2
            rockets_y[i] += rockets_vy[i]
            artist.goto(rockets_x[i], rockets_y[i])
            artist.dot(3, 'white')
            if rockets_vy[i] <= 0:
                launch_burst(rockets_x[i], rockets_y[i], rockets_color[i])
                del rockets_x[i]
                del rockets_y[i]
                del rockets_vy[i]
                del rockets_color[i]

        for i in range(len(particles_x) - 1, -1, -1):
            particles_vy[i] -= 0.12
            particles_vx[i] *= 0.99
            particles_x[i] += particles_vx[i]
            particles_y[i] += particles_vy[i]
            particles_life[i] -= 0.015
            if particles_life[i] > 0:
                artist.goto(particles_x[i], particles_y[i])
                artist.dot(particles_life[i] * 4, particles_color[i])
            if particles_life[i] <= 0 or particles_y[i] < -300:
                del particles_x[i]
                del particles_y[i]
                del particles_vx[i]
                del particles_vy[i]
                del particles_color[i]
                del particles_life[i]

        screen.update()
except turtle.Terminator:
    pass