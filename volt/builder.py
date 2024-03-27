import os
from tkinter import Label, Button, StringVar

class FileCounterApp:
    def __init__(self, master):
        self.master = master
        master.title("File Counter")

        self.directory_path = StringVar()
        self.directory_path.set(os.getcwd())

        self.label = Label(master, text="Directory:")
        self.label.grid(row=0, column=0)

        self.directory_label = Label(master, textvariable=self.directory_path)
        self.directory_label.grid(row=0, column=1)

        self.count_button = Button(master, text="Count Files", command=self.count_files)
        self.count_button.grid(row=1, column=0, columnspan=2)

        self.result_label = Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2)

    def count_files(self):
        directory = self.directory_path.get()
        if not os.path.isdir(directory):
            self.result_label.config(text="Invalid directory path!")
            return

        file_count = sum(len(files) for _, _, files in os.walk(directory))
        self.result_label.config(text=f"Total files: {file_count}")
