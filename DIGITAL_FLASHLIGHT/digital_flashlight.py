import tkinter as tk

def toggle_flashlight():
    if flashlight_window.attributes('-alpha') == 1.0:
        flashlight_window.attributes('-alpha', 0.0)  # Hide
    else:
        flashlight_window.attributes('-alpha', 1.0)  # Show

flashlight_window = tk.Tk()
flashlight_window.attributes('-fullscreen', True)  # Fullscreen mode
flashlight_window.configure(bg='white')  # White background

# Close the flashlight window with Esc key
flashlight_window.bind("<Escape>", lambda e: flashlight_window.quit())

# Toggle flashlight on clicking the window
flashlight_window.bind("<Button-1>", lambda e: toggle_flashlight())

flashlight_window.mainloop()
