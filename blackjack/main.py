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

def show_player_card_values():
    """Prints the cards and the value of them for the player.
    """
    print(f"Your cards: {player_cards}, current score: {player_cards_value}")

def show_cpu_card_values():
    """Prints the cards and the value of them for the CPU.
    """
    print(f"Your cards: {cpu_cards}, score: {cpu_cards_value}")

def show_cpu_starting_hand():
    cpu_shown_card = cpu_cards[0]
    print(f"Computer's first card: {cpu_shown_card}")

# Debug info - card value
# print(calculate_card_value(player_cards))

calculate_card_value(player_cards)

# Anyone has Blackjack from the start?
cpu_cards_value = calculate_card_value(cpu_cards)
player_cards_value = calculate_card_value(player_cards)
if cpu_cards_value == 21:
    print("Game Over. Computer has Blackjack!")
elif player_cards_value == 21:
    print("Game Over. You have Blackjack!")
else:
    show_player_card_values()
    show_cpu_starting_hand()

    more_card_choice = input("Type 'y' to get another card, type 'n' to pass:\t")
    while more_card_choice == 'y':
        player_cards.extend(random.choices(cards))
        player_cards_value = calculate_card_value(player_cards)
        show_player_card_values()
        show_cpu_starting_hand()

# This part needs fixing
        if player_cards_value > 21:
            print("Game Over. Computer has won!")
            more_card_choice = 'n'
        else:
            more_card_choice = input("Type 'y' to get another card, type 'n' to pass:\t")
# here

    cpu_more_card_choice = True
    while cpu_more_card_choice:
        if cpu_cards_value < 16:
            cpu_cards.extend(random.choices(cards))
            cpu_cards_value = calculate_card_value(cpu_cards)
            # print(f"debug info - cpu_cards: {cpu_cards}")
        else:
            cpu_more_card_choice = False

    if cpu_cards_value > 21:
        print("Game Over. You have won!")
        show_cpu_card_values()
    else:
        # Determine who has won
        if cpu_cards_value == player_cards_value:
            print(f"cpu_cards: {cpu_cards}")
            print(f"player_cards: {player_cards}")
            print("Game Over. This is a draw.")
        elif cpu_cards_value > player_cards_value:
            print(f"cpu_cards: {cpu_cards}")
            print("Game Over. Computer has won!")
        elif cpu_cards_value < player_cards_value:
            print(f"cpu_cards: {cpu_cards}")
            print("Game Over. You have won!")
