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
print(type(data))
# print(data["temp"])

# Convert to dictionary
data_dict = data.to_dict()
print(data_dict)

# Get average
temp_list = data["temp"].to_list()
print(temp_list)
average_temp = "{:.2f}".format(sum(temp_list) / len(temp_list))
print(average_temp)

# Use pandas to get average (mean)
pandas_average = data["temp"].mean()
print(pandas_average)

# Use pandas to get maximum
pandas_maximum = data["temp"].max()
print(pandas_maximum)

# Get data in columns
print(data["condition"])
print(data.condition)  # it's the same as above

print("----------------------------------------------------------------------------------------")

# Get data in row
print(data[data.day == "Monday"])

# Print the row of data where it had the highest temperature
print(data[data.temp == data.temp.max()])

# Simplifying getting data out of a specific row
monday = data[data.day == "Monday"]
print(monday.condition)

# Get Monday's temperature in Fahrenheit
print((monday.temp * 9/5) + 32)


# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Ferko"],
    "scores": [76, 56, 12]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")

