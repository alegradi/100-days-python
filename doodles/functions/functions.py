### Basic function ###

def say_something():
    print("something!")

say_something()

#################################################

### Passing information to a function ###

def print_message(message):
    print(message)

print_message("ferko!")

#################################################

### Use positional arguments ###

def describe_animal(animal, name):
    """Display information about a pet."""
    print("I have an " + animal + ".")
    print("It's called " + name + ".")

describe_animal("cicus", "cirmi")

#################################################

### Use keyword arguments ###

def describe_boats(boat_type, displacement):
    """Display information about a boat."""
    print("I have a(n) " + boat_type + ".")
    print("It's displacing " + displacement)

describe_boats(displacement="2000", boat_type="Canu")
describe_boats(boat_type="yacht", displacement="50000")

#################################################

### Set default to a parameter ###

def describe_bridges(bridge_colour, bridge_type='chain'):
    print("Bridge type is " + bridge_type + ".")
    print("Bridge colour is " + bridge_colour + ".")

describe_bridges(bridge_type='swing', bridge_colour='red')
describe_bridges(bridge_colour='orange')

#################################################

### Make an argument optional ###

def describe_bridges2(bridge_colour, bridge_type=None):
    if bridge_type:
        print("Bridge type is " + bridge_type + ".")

    print("Bridge colour is " + bridge_colour + ".")

describe_bridges2(bridge_type='swing', bridge_colour='blue')
describe_bridges2(bridge_colour='pink')

#################################################

### Use function to return value ###

def build_person(first, last):
    """Print a person's full name"""
    person = (first + " " + last)
    return person.title()

famous_person = build_person("ferko", "ferdinand")
print(famous_person)

#################################################

### Use function to return a dictionary ###

def build_house(size, bedrooms):
    """Build a house with given parameters."""
    house = {"Size:": size, "Bedrooms:": bedrooms}
    return house

random_house_1 = build_house("80", "4")
print(random_house_1)

#################################################

### Use function to return a dictionary with optional values ###

def build_ship(name, type, tonnage, home_port=None, registration=None):
    """Build a ship with the provided parameters"""
    built_ship = {"Name": name, "Type": type, "Tonnage": tonnage}
    if home_port:
        built_ship['Home Port'] = home_port
    elif registration:
        built_ship['Registration'] = registration
    return built_ship

summit_explorer = build_ship(name="Summit explorer", type="Bulk carrier", tonnage="20K", home_port="Singapore")
pixie = build_ship("pixie", "Container ship", "15K", registration="Liberia")
print(summit_explorer)
print(pixie)

#################################################

### Pass a list in as an argument ###

def collect_pokemons(pokemons):
    """Collects Pokemons"""
    for pokemon in pokemons:
        print("I caught: " + pokemon.title() + "!")

beasties = ["raichu", "seel", "dewgong"]
collect_pokemons(beasties)

#################################################

### Allow a function to modify a list ###

## Commented out to work on the below example (prevent)

# def print_4d_models(unprinted, printed):
#     """Print 4D models"""
#     while unprinted:
#         current_model = unprinted.pop()
#         print("Printing: " + current_model)
#         printed.append(current_model)

# # Store some unprinted models
# unprinted = ["Chess", "BUK", "Supersonic Booze Carrier"]
# printed = []

# print_4d_models(unprinted, printed)
# print("Unprinted models: ", unprinted)
# print("Printed models: ", printed)

#################################################

### Prevent a function to modify a list ###

def sink_ships(not_sunk, sunk):
    """Sink ships"""
    while not_sunk:
        current_ship = not_sunk.pop()
        print("Sinking: " + current_ship + "!" )
        sunk.append(current_ship)

# Store some ships
original_ships = ["Quenie", "Moskva", "Dzhankoi"]
sunk = []

sink_ships(original_ships[:], sunk)  ## <<<<<<<<<<-------------- What's this?
print("Original ships: ", original_ships)
print("Sunk ships: ", sunk)

#################################################

### Collect an arbitrary number of arguments ###

def make_pizza(size, *toppings):
    """Bake specified pizzas."""
    print("Making a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

# Make 3 pizzas with different toppings
make_pizza("Large", "Ham", "Pineaplle")
make_pizza("Medium", "Pepperoni", "Blue Cheese")
make_pizza("Extra large", "Sour Cream", "Garlic", "Chicken breast fillet")

#################################################

### Collect an arbitrary number of keyword arguments ###

def build_profile(first, last, **user_info):
    """Specify first name, last name and key-value pairs like achievement='Genius'"""
    profile = {"First": first, "Last": last}
    for key, value in user_info.items():
        profile[key] = value

    return profile

# Specify 2 people
mao_zedong = build_profile("Mao", "Zedong", personal_info="Peadophile", personal_info2="Dictator")
genghis_khan = build_profile("Genghis", "Khan", rank="Khan", achivement="Exterminator")

print(mao_zedong)
print(genghis_khan)


