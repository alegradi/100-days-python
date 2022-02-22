rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

handy = [rock, paper, scissors]

lost = "You lose"
win = "You won!"
draw = "It's a draw"

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(handy[player])

computer = random.randint(0, 2)
print("Computer chose:")
print(handy[computer])

rock = [draw, lost, win]
paper = [win, draw, lost]
scissors = [lost, win, draw]
result = [rock, paper, scissors]

print(result[player][computer])
