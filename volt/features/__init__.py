import tkinter as tk
from model import *
from data_prep import *
from ui import *
from image_frame import *

class DataModelAppController:
    def __init__(self, file_path, png_path):
        self.file_path = file_path
        self.png_path = png_path

    def run(self):
        reader = CSVReader(self.file_path)
        data = reader.read()

        algorithm = "kmeans"
        parameters = {"n_clusters": 2}

        cluster_data_an = cluster_data(data, algorithm, parameters)
        print(cluster_data_an)

        root = tk.Tk()
        app = DataModelApp(root)
        image_frame = ImageFrame(root,self.png_path)
        image_frame.pack()
        root.mainloop()

if __name__ == "__main__":
    file_path = "volt/assets/california_housing_test.csv"
    png_path = "volt/assets/example.png"
    app_controller = DataModelAppController(file_path, png_path)
    app_controller.run()
