import tkinter as tk
import random
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
PARTICLE_COUNT_PER_FRAME = 5
UPDATE_DELAY_MS = 16  # Delay in milliseconds (~60 FPS)
BACKGROUND_COLOR = "black"

# --- Particle Class ---
class Particle:
    """
    Represents a single particle.
    It has a position, velocity, base color, and lifespan.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # Generate a random angle and speed
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 4)
        
        # Convert polar coordinates to cartesian velocity
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # Store the original, bright color components
        self.base_r = random.randint(100, 255)
        self.base_g = random.randint(100, 255)
        self.base_b = random.randint(100, 255)
        
        self.max_lifespan = random.randint(40, 100)
        self.lifespan = self.max_lifespan

    def update(self):
        """
        Update particle's position and decrease its lifespan.
        Returns True if the particle is still alive, False otherwise.
        """
        self.x += self.vx
        self.y += self.vy
        self.lifespan -= 1
        return self.lifespan > 0

    def get_faded_color(self):
        """
        Calculates the current faded color as a hex string for Tkinter.
        """
        if self.lifespan <= 0:
            return ""
            
        # Calculate the fade ratio (from 1.0 down to 0.0)
        fade_ratio = self.lifespan / self.max_lifespan
        
        # Calculate the new color by scaling the original color
        r = int(self.base_r * fade_ratio)
        g = int(self.base_g * fade_ratio)
        b = int(self.base_b * fade_ratio)
        
        # Format as a Tkinter-compatible hex string (e.g., #RRGGBB)
        return f"#{r:02x}{g:02x}{b:02x}"

# --- Global list to hold all active particles ---
particles = []

def simulation_loop():
    """
    This function runs one frame of the simulation.
    It updates, draws, and then schedules itself to run again.
    """
    # 1. Clear the canvas of all previous drawings
    canvas.delete("all")
    
    # 2. Create new particles for this frame
    for _ in range(PARTICLE_COUNT_PER_FRAME):
        particles.append(Particle(CENTER_X, CENTER_Y))
        
    # 3. Update, filter, and draw all particles
    alive_particles = []
    for p in particles:
        if p.update():  # update() returns True if particle is still alive
            alive_particles.append(p)
            
            # Get the particle's current color
            color = p.get_faded_color()
            
            # Define the 3x3 pixel rectangle (oval)
            x1, y1 = p.x - 1.5, p.y - 1.5
            x2, y2 = p.x + 1.5, p.y + 1.5
            
            # Draw the particle on the canvas
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")

 
    particles[:] = alive_particles
    
    # 4. Schedule this function to run again after the delay
    root.after(UPDATE_DELAY_MS, simulation_loop)

# --- Main Application Setup ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Particle Simulation (Tkinter)")
    root.resizable(False, False)

    canvas = tk.Canvas(
        root, 
        width=SCREEN_WIDTH, 
        height=SCREEN_HEIGHT, 
        bg=BACKGROUND_COLOR,
        highlightthickness=0
    )
    canvas.pack()

    # Start the simulation loop
    simulation_loop()

    # Run the Tkinter main event loop
    root.mainloop()