import math

def draw_mandala(width=60, height=30, layers=5):
    """Draw a mandala-like ASCII pattern using math functions."""
    center_x = width // 2
    center_y = height // 2
    pattern = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Draw multiple rose curves (r = sin(n * theta)) for layers
    for n in range(1, layers + 1):
        a = 10 * n  # Amplitude
        for theta_deg in range(0, 360 * 4, 1):  # Oversample for smoothness
            theta = math.radians(theta_deg)
            r = a * abs(math.sin(n * theta))  # Rose curve
            
            x = center_x + int(r * math.cos(theta))
            y = center_y + int(r * math.sin(theta))
            
            if 0 <= x < width and 0 <= y < height:
                # Use different chars for layers
                char = ['.', '-', '*', '+', '#'][n % 5]
                pattern[y][x] = char
    
    # Add concentric circles
    for ring in range(1, min(center_x, center_y) // 3):
        r = ring * 3
        for theta_deg in range(0, 360, 5):
            theta = math.radians(theta_deg)
            x = center_x + int(r * math.cos(theta))
            y = center_y + int(r * math.sin(theta))
            if 0 <= x < width and 0 <= y < height:
                pattern[y][x] = '|'
    
    # Print the pattern
    for row in pattern:
        print(''.join(row))

def main():
    size = input("Enter size (default 60x30): ").strip()
    if size:
        try:
            w, h = map(int, size.split('x'))
        except ValueError:
            w, h = 60, 30
    else:
        w, h = 60, 30
    
    layers = input("Number of layers (default 5): ").strip()
    layers = int(layers) if layers.isdigit() else 5
    
    print("\nMandala Pattern:\n")
    draw_mandala(w, h, layers)
    print()

if __name__ == "__main__":
    main()
