import tkinter as tk

class ControlPanel(tk.Frame):
    """Panel with control buttons and the list of frames."""
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller

        # Tkinter variables for inputs
        self.duration_var = tk.IntVar(value=500)
        self.loop_var = tk.IntVar(value=0)

        self._build_widgets()

    def _build_widgets(self):
        """Creates and places widgets in the control panel."""
        tk.Button(self, text="Add Images", width=20, command=self.controller.add_images).pack(pady=4)
        tk.Button(self, text="Remove Selected", width=20, command=self.controller.remove_selected).pack(pady=4)
        tk.Button(self, text="Move Up", width=20, command=lambda: self.controller.move_selected(-1)).pack(pady=4)
        tk.Button(self, text="Move Down", width=20, command=lambda: self.controller.move_selected(1)).pack(pady=4)

        # Section for duration and loop
        tk.Label(self, text="Frame duration (ms)").pack(pady=(12, 0))
        tk.Entry(self, textvariable=self.duration_var, width=10).pack()

        tk.Label(self, text="Loop count (0 = infinite)").pack(pady=(8, 0))
        tk.Entry(self, textvariable=self.loop_var, width=10).pack()

        # Save button
        tk.Button(self, text="Save GIF", width=20, command=self.controller.save_gif).pack(pady=(12,4))

        # Frames list
        tk.Label(self, text="Frames (order shown)").pack(pady=(12, 0))
        self.listbox = tk.Listbox(self, width=40, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=4, fill=tk.BOTH, expand=True)

    def update_listbox(self, items, selection_index=None):
        """Clears and repopulates the frames listbox."""
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)
        if selection_index is not None:
            self.listbox.select_set(selection_index)
            self.listbox.activate(selection_index)