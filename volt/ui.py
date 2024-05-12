import tkinter as tk

class DataModelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UI")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.select_data_button = tk.Button(self.main_frame, text="Select Data", command=self.open_select_data)
        self.select_data_button.pack()

        self.run_model_button = tk.Button(self.main_frame, text="Run Model", command=self.open_run_model)
        self.run_model_button.pack()

        self.show_results_button = tk.Button(self.main_frame, text="Show Results", command=self.open_show_results)
        self.show_results_button.pack()

    def open_select_data(self):
        select_data_frame = tk.Toplevel(self.root)
        select_data_frame.title("Select Data")

    def open_run_model(self):
        run_model_frame = tk.Toplevel(self.root)
        run_model_frame.title("Run Model")

    def open_show_results(self):
        show_results_frame = tk.Toplevel(self.root)
        show_results_frame.title("Show Results")

