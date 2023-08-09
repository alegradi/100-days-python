import csv

# Read line-by-line the contents of the file
# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#
# print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data_file, None)  # Skip the header 'temp'
#     temperatures = []
#
#     for row in data:
#         temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])



