import csv
def read_report(weather):

    with open("weather_1.csv","r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()

weather = read_report("/home/sheryar/Documents/github/WeatherTask/weather_1.csv")