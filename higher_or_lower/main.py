import random
import os
from art import higher_or_lower, vs
from game_data import data as data_list

clear = lambda: os.system('clear')

# Global variables

GAME_DATA_INDEX = data_list
HIGHSCORE = 0
GAME_OVER = False
OPTION_A = ""
OPTION_B = ""

# Function Definitions

def format_entry_info(index_no):
    """
    Requires 'index_no' as argument.
    Returns a, formatted_entry_info
    returns b, debug_info (follower count)
    """
    entry_name = data_list[index_no]['name']
    entry_followers = data_list[index_no]['follower_count']
    entry_type = data_list[index_no]['description']
    entry_location = data_list[index_no]['country']

    formatted_entry_info = str(f"{entry_name} is {entry_type} from {entry_location}.")
    debug_info = str(f"{entry_name} has {entry_followers} million followers")
    return formatted_entry_info, debug_info

def get_random_entry():
    """Pops a random number from 'list_of_index_numbers'"""
    random_entry = random.choice(list_of_index_numbers)
    list_of_index_numbers.remove(random_entry)
    return random_entry

def compare_follower_count(index1, index2):
    """Compares the follower count from the list of dictionaries in
    game_data.py
    Returns the higher value index."""
    follower_count_1 = int(data_list[index1]['follower_count'])
    follower_count_2 = int(data_list[index2]['follower_count'])
    if follower_count_1 > follower_count_2:
        return index1
    else:
        return index2

def display_options(option_a, option_b):
    print(f"A: {option_a}")
    print(vs)
    print(f"B: {option_b}")

def a_becomes_b(option_a, option_b):
    option_a = option_b
    option_b = get_random_entry()
    return option_a, option_b

def game(option_a, option_b):
    """The game function"""
    global HIGHSCORE
    global GAME_OVER

    display_a, debug_a = format_entry_info(option_a)
    display_b, debug_b = format_entry_info(option_b)

    display_options(display_a, display_b)

    # Compare the two entries
    larger_count = compare_follower_count(option_a, option_b)
    # print(larger_count)  ## Debug info

    # Ask the user for input, A or B. Who has more followers?
    player_choice = str(input("\nWhich one has more followers? Select 'a' or 'b': "))

    # Probably very convuluted way of checking if player choice is correct or not.
    choice_to_index = {'a': option_a, 'b': option_b}

    if player_choice == 'a' or 'b':
        if choice_to_index[player_choice.lower()] == larger_count:
            # print("Player selected the correct one") ## Debug info
            # Clear the screen
            clear()
            HIGHSCORE = HIGHSCORE + 1
            print(higher_or_lower)
            print(f"You are right! Current score is: {HIGHSCORE}")
        else:
            # print("Player selected the incorrect one")  ## Debug info
            print("Sorry that's incorrect!")
            print(f"Your final score is: {HIGHSCORE}")
            print("Hint for next time: \n")
            display_options(debug_a, debug_b)
            GAME_OVER = True
            return GAME_OVER
    else:
        print("You have not typed a valid option! Quitting.")
        GAME_OVER = True
        return GAME_OVER

## Gameplay ##

# Create a list of index numbers to work with
list_of_index_numbers = []
for _ in range(0, 50):
    list_of_index_numbers.append(_)

# Display 'higher or lower' art and welcome message
clear()
print("Welcome to: \n")
print(higher_or_lower)
print("The goal is to select A or B, whichever has higher instagram follower count.\n")

OPTION_A = get_random_entry()
OPTION_B = get_random_entry()

# Game loop until incorrect answer is given
while not GAME_OVER:
    game(OPTION_A, OPTION_B)
    OPTION_A, OPTION_B = a_becomes_b(OPTION_A, OPTION_B)
