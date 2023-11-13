import csv

def read_csv(csv_file, number_plate):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['number_plate'] == number_plate:
                return row
        return None
