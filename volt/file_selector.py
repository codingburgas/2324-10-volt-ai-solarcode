import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FileSelectionFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.selected_files = []
        self.current_dir = os.getcwd()

        self.create_widgets()

    def create_widgets(self):
        # Directory display label
        self.directory_label = tk.Label(self, text=f"Current directory: {self.current_dir}")
        self.directory_label.pack()

        # File list frame
        self.file_list_frame = tk.Frame(self)
        self.file_list_frame.pack()
        self.populate_file_list()

        # Navigation buttons
        self.up_button = tk.Button(self, text="Up", command=self.go_up_dir)
        self.up_button.pack()

        self.select_button = tk.Button(self, text="Select Files", command=self.select_files)
        self.select_button.pack()

    def populate_file_list(self):
        # Clear existing entries
        for widget in self.file_list_frame.winfo_children():
            widget.destroy()

        # Add files and directories
        for item in os.listdir(self.current_dir):
            path = os.path.join(self.current_dir, item)
            if os.path.isfile(path):
                label = tk.Label(self.file_list_frame, text=item)
                label.bind("<Button-1>", lambda event, f=path: self.toggle_selection(f))
                label.pack()
            elif os.path.isdir(path):
                label = tk.Label(self.file_list_frame, text=item + " (dir)")
                label.bind("<Button-1>", lambda event, d=path: self.open_directory(d))
                label.pack()

    def toggle_selection(self, file_path):
        if file_path in self.selected_files:
            self.selected_files.remove(file_path)
        else:
            self.selected_files.append(file_path)

    def open_directory(self, directory):
        self.current_dir = directory
        self.directory_label.config(text=f"Current directory: {self.current_dir}")
        self.populate_file_list()

    def go_up_dir(self):
        parent_dir = os.path.dirname(self.current_dir)
        if parent_dir:
            self.current_dir = parent_dir
            self.directory_label.config(text=f"Current directory: {self.current_dir}")
            self.populate_file_list()

    def select_files(self):
        if not self.selected_files:
            messagebox.showwarning("No files selected", "Please select at least one file.")
            return

        # Return the selected files as a list
        root.destroy()

# Example usage
root = tk.Tk()
file_selection_frame = FileSelectionFrame(root)
file_selection_frame.pack()
root.mainloop()

print(file_selection_frame.selected_files)