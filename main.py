"""
The main module of the application. Connects the builder, the UI, and the data.
"""
import os
from tkinter import Tk, Label, Button, StringVar
import csv

import csv

class CSVReader:
    def read_csv(self, file_path):
        try:
            with open(file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                data = []
                for row in csv_reader:
                    data.append(row)
                return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error occurred while reading file '{file_path}': {e}")
            return None
        

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

# Пример!?!
if __name__ == "__main__":
    csv_reader = CSVReader()
    file_path = "example.csv"
    data = csv_reader.read_csv(file_path)
    if data:
        print("CSV Data:")
        for row in data:
            print(row)
