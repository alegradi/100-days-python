# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }

# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary

# print(final_dictionary)

# for key in final_dictionary:
#     final_dictionary[key] += 1

# print(final_dictionary)

#--------------------------#---------------------#

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2][0])

#--------------------------#---------------------#

bidder_db = {
    "Feri": 3,
    "Jozsi": 4,
    "Maris": 8,
    "Stevo": 41,
}

for bids in bidder_db.items():
    print(bids)

for bids in bidder_db.values():
    print(bids)

highest_bid = 0
for key, value in bidder_db.items():
    print(key, '->', value)
    if value > highest_bid:
        highest_bid = value
        highest_bidder = key

print(f"The highest bidder is {highest_bidder} with {highest_bid}")

