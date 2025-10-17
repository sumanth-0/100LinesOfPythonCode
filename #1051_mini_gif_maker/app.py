import tkinter as tk
from tkinter import filedialog, messagebox
from ui_components import ControlPanel
from gif_processor import GifProcessor


class GifMakerApp(tk.Tk):
    """Main application class acting as the controller."""

    def __init__(self):
        super().__init__()
        self.title("Simple GIF Maker")
        # Reduced geometry because the preview area is removed
        self.geometry("350x500")
        self.resizable(False, False)

        self.processor = GifProcessor()
        self._build_ui()

    def _build_ui(self):
        """Builds the main user interface."""
        # The control panel is now the main element
        self.controls = ControlPanel(self, controller=self)
        self.controls.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Status bar at the bottom
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status(self, text):
        self.status_var.set(text)

    def add_images(self):
        """Opens the dialog to add images."""
        paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
        )
        if not paths: return

        added, errors = self.processor.add_images(paths)
        if errors:
            messagebox.showwarning("Warning", "\n".join(errors))

        self.controls.update_listbox(self.processor.get_frame_basenames())
        self.set_status(f"Added {added} new image(s).")

    def remove_selected(self):
        """Removes the selected image from the list."""
        selection = self.controls.listbox.curselection()
        if not selection: return

        index = selection[0]
        self.processor.remove_image(index)
        self.controls.update_listbox(self.processor.get_frame_basenames())
        self.set_status(f"Removed frame {index + 1}.")

    def move_selected(self, direction):
        """Moves the selected image up or down."""
        selection = self.controls.listbox.curselection()
        if not selection: return

        old_index = selection[0]
        if self.processor.move_image(old_index, direction):
            new_index = old_index + direction
            self.controls.update_listbox(self.processor.get_frame_basenames(), new_index)
            self.set_status("Reordered frames.")

    def save_gif(self):
        """Saves the GIF animation."""
        if not self.processor.frames_images:
            messagebox.showinfo("Info", "No frames to save.")
            return

        try:
            duration = self.controls.duration_var.get()
            loop = self.controls.loop_var.get()
        except tk.TclError:
            messagebox.showerror("Error", "Duration and loop must be integers.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF", "*.gif")])
        if not save_path: return

        try:
            self.processor.save_gif(save_path, duration, loop)
            messagebox.showinfo("Success", f"GIF saved to:\n{save_path}")
            self.set_status(f"Saved GIF: {save_path}")
        except Exception as e:
            messagebox.showerror("Error Saving GIF", str(e))
            self.set_status("Error saving GIF.")
