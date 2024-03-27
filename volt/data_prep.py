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
