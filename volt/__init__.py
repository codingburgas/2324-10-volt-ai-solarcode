import tkinter as tk

class App:
    def __init__(self, ui_frame, data_object, modeling_object):
        self.ui_frame = ui_frame
        self.data_object = data_object
        self.modeling_object = modeling_object

    def run(self):
        self.setup_ui()
        self.load_data()
        self.ui_frame.mainloop()

    def setup_ui(self):
        label = tk.Label(self.ui_frame, text="Welcome to the App")
        label.pack()


    def load_data(self):
        data = self.data_object.load_data()

    def perform_modeling(self):

        self.modeling_object.train_model()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My App")

    data_obj = DataObject()
    modeling_obj = ModelingObject()

    app = App(root, data_obj, modeling_obj)
    app.run()
