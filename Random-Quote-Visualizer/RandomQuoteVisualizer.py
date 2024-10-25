import tkinter as tk
import requests
import random
from tkinter import font
import time

# Fetch a random quote from API
def get_random_quote():
    try:
        # Using ZenQuotes API
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()[0]
        return f'"{data["q"]}"\n- {data["a"]}'
    except:
        return '"Life is what happens while you are busy making other plans."\n- John Lennon'

# Change the background color randomly
def get_random_style():
    colors = [
        ('#1abc9c', '#2ecc71'), ('#3498db', '#2980b9'), 
        ('#e74c3c', '#c0392b'), ('#9b59b6', '#8e44ad'),
        ('#f1c40f', '#f39c12'), ('#2c3e50', '#34495e')
    ]
    fonts = ['Helvetica', 'Arial', 'Times', 'Courier', 'Verdana']
    return random.choice(colors), random.choice(fonts)

# Declare global variables
timer_id = None
last_click_time = 0

# Display the quote in the window
def display_quote(event=None):
    global timer_id
    
    # Prevent double-click
    current_time = time.time() if event else 0
    if event and (current_time - globals().get('last_click_time', 0) < 0.3):
        return
    globals()['last_click_time'] = current_time
    
    # Cancel old timer
    if timer_id:
        window.after_cancel(timer_id)
    
    # Destroy old frame
    for widget in window.winfo_children():
        widget.destroy()
            
    quote = get_random_quote()
    (color1, color2), font_name = get_random_style()
    
    # Create new frame and canvas
    quote_frame = tk.Frame(window, padx=40, pady=40)
    quote_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    canvas = tk.Canvas(quote_frame, width=500, height=300, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(0, 0, 500, 300, fill=color1, width=0)
    
    # Handle quote and font
    quote_text, author = quote.split('\n')
    quote_font_size = 20 if len(quote_text) > 100 else 24
    
    canvas.create_text(250, 120, text=quote_text, 
                      font=(font_name, quote_font_size, 'bold'),
                      width=450, fill='white', justify='center')
    canvas.create_text(250, 250, text=author,
                      font=(font_name, 18, 'italic'),
                      fill='white')
    
    canvas.bind('<Button-1>', display_quote)
    timer_id = window.after(5000, display_quote)

# Create main window
window = tk.Tk()
window.title("Random Quote Visualizer")
window.configure(bg='#2c3e50')  # Dark background

# Set window size and center it
window_width = 800
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Bind click event cho window
window.bind('<Button-1>', display_quote)

# Display the first quote
display_quote()

# Start the tkinter event loop
window.mainloop()




