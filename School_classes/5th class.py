import csv 
with open("/home/hans/Documents/Python/Python/School_classes/data.csv") as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        print(line)