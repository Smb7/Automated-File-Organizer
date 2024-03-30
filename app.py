# main.py

from tkinter import *
from tkinter import filedialog, messagebox
from FileOrganizer import FileOrganizer  # Adjust the import path as necessary

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("File Organizer")

        self.organizer = FileOrganizer()  # Instance of your FileOrganizer

        self.select_button = Button(self, text="Select Directory and Organize", command=self.select_and_organize)
        self.select_button.pack(pady=20)

    def select_and_organize(self):
        directory_path = filedialog.askdirectory()
        if directory_path:  # Proceed only if a directory was selected
            result = self.organizer.organize_files_by_extension(directory_path)
            messagebox.showinfo("Result", result)  # Show the result in a message box

if __name__ == '__main__':
    app = GUI()
    app.mainloop()
