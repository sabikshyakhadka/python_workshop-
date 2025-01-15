import csv

# Read the CSV file
with open("sales_data.csv", mode='r') as file:
    reader = csv.DictReader(file)
    sales_data = [row for row in reader]
