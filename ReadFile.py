import csv
def read_report(file_path):

    with open("weather_1.csv","r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()
    data = []
    with open(file_path,"r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)
    return data
weather = read_report("/home/sheryar/Documents/github/WeatherTask/weather_1.csv")