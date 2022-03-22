# Blackjack
import random
import os
clear = lambda: os.system('clear')
#clear()



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 10, 10, 10]

player_cards = random.choices(cards, k=2)
cpu_cards = random.choices(cards, k=2)

# Debug info - starting cards
print(f"debug info - player_cards: {player_cards}")
print(f"debug info - cpu_cards: {cpu_cards}")

def calculate_card_value(player_cards):
    """Sums up the value of elements from a list. 
    Takes input as the name of list.
    """
    total_card_value = 0
    for card in player_cards:
        total_card_value += card

    return total_card_value

# Debug into - card value
print(calculate_card_value(player_cards))

calculate_card_value(player_cards)

# Anyone has Blackjack from the start?
cpu_cards_value = calculate_card_value(cpu_cards)
player_cards_value = calculate_card_value(player_cards)
if cpu_cards_value == 21:
    print("Game Over. Computer has Blackjack!")
elif player_cards_value == 21:
    print("Game Over. You have Blackjack!")

def show_card_values():
    """Prints the cards and the value of them for the player.
    Prints the computer's first hand
    """
    print(f"Your cards: {player_cards}, current score: {player_cards_value}")
    cpu_shown_card = cpu_cards[0]
    print(f"Computer's first card: {cpu_shown_card}")



show_card_values()

more_card_choice = input("Type 'y' to get another card, type 'n' to pass:\t")
while more_card_choice == 'y':
    player_cards.extend(random.choices(cards))
    player_cards_value = calculate_card_value(player_cards)
    show_card_values()
    if player_cards_value > 21:
        print("Game Over. Computer has won!")
    else:
        more_card_choice = input("Type 'y' to get another card, type 'n' to pass:\t")

cpu_more_card_choice = True
while cpu_more_card_choice:
    if cpu_cards_value < 16:
        cpu_more_card_choice = True
        cpu_cards.extend(random.choices(cards))
        cpu_cards_value = calculate_card_value(cpu_cards)
        print(f"debug info - cpu_cards: {cpu_cards}")
    else:
        cpu_more_card_choice = False


