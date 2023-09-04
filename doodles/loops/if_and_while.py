### Value in list ###

cats = ['fluffy', 'mr rogers', 'sox']

sox_in_cats = 'sox' in cats
print(sox_in_cats)
print('fluff' in cats)

#################################################

### Check if a list is empty ###

actresses = ['yolan']

if actresses:
    for actress in actresses:
        print("Actress: " + actress.title())
else:
    print("There are no actresses!")

#################################################

### Write a while loop ###

pears = 5

while pears >= 0:
    print(f"We have {pears} pears left.")
    pears -= 1

#################################################

### While loop broken by user input ###

continue_loop = True

while continue_loop:
    print("This loop is still ongoing!")
    decision = input("Do you want to continue? y/n")

    if decision == "n":
        continue_loop = False

#################################################

### While loop broken by break ###

prompt = "What cities have you visited? "
prompt += "When you're done type 'quit'. "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I've been to " + city + " !")

#################################################

### Use continue in loop ###

banned_users = ['fred', 'anthony', 'matt']

prompt = "Add a user to your team. Type 'quit' when done. "

players = []

while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print("This user is banned!")
        continue
    else:
        players.append(player)

print("Your team:")
for player in players:
    print(f" - {player}")


#################################################

### Remove item from list ###

animals = ['cat', 'dog', 'giraffe', 'cat', 'hippo', 'cat']

print(animals)

while "cat" in animals:
    animals.remove("cat")

print(animals)
