# Blackjack
import random
import os
clear = lambda: os.system('clear')
#clear()



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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

calculate_card_value(player_cards)
