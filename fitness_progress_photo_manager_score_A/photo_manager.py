import os
import datetime
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class FitnessProgressPhotoManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Progress Photo Manager")
        self.photos = []

        self.date_label = Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = Entry(root)
        self.date_entry.pack()

        self.photo_label = Label(root, text="Photo Path:")
        self.photo_label.pack()
        self.photo_entry = Entry(root)
        self.photo_entry.pack()

        self.note_label = Label(root, text="Notes:")
        self.note_label.pack()
        self.note_entry = Entry(root)
        self.note_entry.pack()

        self.upload_button = Button(root, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack()

        self.view_button = Button(root, text="View Progress", command=self.view_photos)
        self.view_button.pack()

    def upload_photo(self):
        date = self.date_entry.get()
        photo_path = self.photo_entry.get()
        notes = self.note_entry.get()

        if not date or not photo_path:
            messagebox.showwarning("Input Error", "Please enter both date and photo path.")
            return

        if not self.validate_date(date):
            messagebox.showwarning("Input Error", "Please enter a valid date (YYYY-MM-DD).")
            return

        if not os.path.exists(photo_path):
            messagebox.showwarning("Input Error", "Photo path does not exist.")
            return

        self.photos.append({"date": date, "photo": photo_path, "notes": notes})
        messagebox.showinfo("Success", "Photo uploaded successfully!")

    def view_photos(self):
        if not self.photos:
            messagebox.showinfo("No Photos", "No photos uploaded yet.")
            return
        
        progress_report = "Progress Photos:\n\n"
        for photo in self.photos:
            progress_report += f"Date: {photo['date']}, Photo: {photo['photo']}, Notes: {photo['notes']}\n"
        
        messagebox.showinfo("Progress Report", progress_report)

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

def main():
    root = Tk()
    manager = FitnessProgressPhotoManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
