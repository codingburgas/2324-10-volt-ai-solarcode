import csv

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        data = []
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
        return data

