import tkinter as tk
from PIL import Image, ImageTk

class ImageFrame(tk.Frame):
    def __init__(self, master, image_path):
        super().__init__(master)
        self.image_path = image_path

        self.load_image()

    def load_image(self):
        try:
            image = Image.open(self.image_path)
            photo_image = ImageTk.PhotoImage(image)

            label = tk.Label(self, image=photo_image)
            label.image = photo_image
            label.pack()
        except FileNotFoundError:
            label = tk.Label(self, text="Image not found")
            label.pack()
        except Exception as e:
            label = tk.Label(self, text=f"Error loading image: {e}")
            label.pack()

