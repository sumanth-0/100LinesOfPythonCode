import tkinter as tk
from gui import WaterTrackerApp

# Launches water intake app
def main():
    root = tk.Tk()
    app = WaterTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()