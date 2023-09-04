
alien0 = {"color": "green", "points": 5}

### Get value of key ###

alien0_color = alien0["color"]
print(alien0_color)

#################################################

### Use get function for the above

print(alien0.get("color"))
print(alien0.get("address", "Does not exist"))

#################################################

### Add the `"location": "at home"` to the dictionary ###

alien0["location"] = "at home"
print(alien0)

#################################################

### Modify the value of "color" ###

alien0["color"] = "yellow"
print(alien0)

#################################################

### Delete the key-value pair `location` ###

del alien0["location"]
print(alien0)

#################################################

### Loop through all key-value pairs ###

fav_languages = {"edward": "python", "frank": "c+", "joe": "php", "dane": "go"}

for name, language in fav_languages.items():
    print(name + ": " + language)

#################################################

### Loop through the names ###

for name in fav_languages.keys():
    print(name)

#################################################

### Loop through the languages ###

for language in fav_languages.values():
    print(language)

#################################################

### How many items in the above list ###

print(len(fav_languages))

#################################################

### Define a list of dictionaries ###

list_of_dict = [fav_languages, alien0]
print(list_of_dict)

print("------------===================================-------------")

#################################################

### Use for loop to print all elements of a list of dictionaries ###

users = []

new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi'
}

users.append(new_user)

new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie'
}

users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")

#################################################

### Lists in a dictionary ###

food = {"pizza": ["pepperoni", "hawai", "vegan"], "fries": ["chips"]}

for category, food_types in food.items():
    print(category + ": ")
    for food_type in food_types:
        print(food_type)

#################################################

### Dictionary within a dictionary ###

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris"
    }
}

for username, user_dicto in users.items():
    print("\nUsername: " + username)
    full_name = user_dicto["first"] + " "
    full_name += user_dicto["last"]
    location = user_dicto["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#################################################

### Create an ordered directory ###

from collections import OrderedDict

names = []
languages = []

second_fav_languages = OrderedDict()
second_fav_languages["jen"] = ["python", "ruby"]
second_fav_languages["feri"] = ["rust"]
second_fav_languages["zalan"] = ["python", "go"]

for names, langs in second_fav_languages.items():
    print(names.title() + ": ")
    for languages in langs:
        print("- " + languages)

#################################################

### Create a list of dictionaries with 1M items ###

trees = []

for tree_num in range(1000000):
    new_tree = {}
    new_tree["leaves"] = tree_num
    new_tree["type"] = "oak"
    new_tree["size"] = tree_num
    trees.append(new_tree)

print("Total number of trees: ")
print(len(trees))

print(trees[0])