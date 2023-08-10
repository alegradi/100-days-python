import pandas


# Get the sum of squirrels based on their fur colours
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Sum of Gray squirrels
grey_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]


# Sum of Red squirrels
red_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

# Sum of Black squirrels
black_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]


squirrel_count_data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(grey_squirrel), len(red_squirrel), len(black_squirrel)]
}

squirrel_count = pandas.DataFrame(squirrel_count_data_dict)
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")


