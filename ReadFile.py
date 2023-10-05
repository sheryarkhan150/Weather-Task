import csv

file = open("weather_1.csv")
csvreader = csv.DictReader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
