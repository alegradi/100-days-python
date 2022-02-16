print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction_1 = input("\nWhich way would you like to go? Please select 'forward' or 'left' \n").lower()
if direction_1 == "forward":
  print("\nYou are moving forward and find yourself facing a door. What would you like to do?")
  direction_2 = input("\nPlease select 'wait' for someone to open the door for you or 'force' yourself in.\n").lower()

  if direction_2 == "force":
    print("\nYou have successfully forced yourself through the door!")

    direction_3 = input("\n You are on a big grass meadow. Please select 'run' to quickly cross it or 'walk' to take your time.\n").lower()

    if direction_3 == "run":
      print("\nYou have crossed the field!")

    if direction_3 == "walk":
      print("\n You are taking your time to cross the field.")
      print("Oh no a biplane is diving on you, firing it's cannon!")
      print("Game over!")
    else:
      print("You were not able to follow simple instructions. Game over!")

  if direction_2 == "wait":
    print("\nYou wait there for all eternety and a bit more.")
    print("\nGame over!")
  else:
    print("You were not able to follow simple instructions. Game over!")

if direction_1 == "left":
  print("What are you going to the left for? You ran into a cactus!")
  print("Game over!")
# else:
#   print("You were not able to follow simple instructions. Game over!")
