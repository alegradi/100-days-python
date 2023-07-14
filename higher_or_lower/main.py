import random
from art import higher_or_lower, vs
from game_data import data as data_list

# Global variables

GAME_DATA_INDEX = data_list
HIGHSCORE = 0
GAME_OVER = False

# Function Definitions

def print_entry_info(index_no):
    """Returns information from a list of dictionaries
    Requires 'index_no' as argument."""
    entry_name = data_list[index_no]['name']
    entry_followers = data_list[index_no]['follower_count']
    entry_type = data_list[index_no]['description']
    entry_location = data_list[index_no]['country']

    print(f"Psst: {entry_name} has {entry_followers} million followers")  ## Debug print
    print(f"{entry_name} is {entry_type} from {entry_location}.")

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

def game():
    """The game function"""
    global HIGHSCORE
    global GAME_OVER

    # Use random generator to pick two random entries from the list
    random_index_1 = get_random_entry()
    random_index_2 = get_random_entry()

    # Display option A with info, vs art and option B with info
    print("A,")
    print_entry_info(random_index_1)
    print(vs)
    print("B,")
    print_entry_info(random_index_2)

    # Compare the two entries
    larger_count = compare_follower_count(random_index_1, random_index_2)
    # print(larger_count)  ## Debug info

    # Ask the user for input, A or B. Who has more followers?
    player_choice = str(input("\nWhich one has more followers? Select 'a' or 'b': "))

    # Probably very convuluted way of checking if player choice is correct or not.
    choice_to_index = {'a': random_index_1, 'b': random_index_2}

    if player_choice == 'a' or 'b':
        if choice_to_index[player_choice.lower()] == larger_count:
            # print("Player selected the correct one") ## Debug info
            HIGHSCORE = HIGHSCORE + 1
            print(f"Your score is: {HIGHSCORE}")
        else:
            # print("Player selected the incorrect one")  ## Debug info
            print("Sorry that's incorrect!")
            print(f"Your final score is: {HIGHSCORE}")
            GAME_OVER = True
            return GAME_OVER
    else:
        print("You have not typed a valid option! Quitting.")
        GAME_OVER = True
        return GAME_OVER






### TODO ###

# Create a list of index numbers to work with
list_of_index_numbers = []
for _ in range(0, 50):
    list_of_index_numbers.append(_)

# Display 'higher or lower' art and welcome message

print("Welcome to: \n")
print(higher_or_lower)
print("The goal is to select A or B, whichever has higher instagram follower count.\n")


# Also now compare to a random one the one you won with


# Game loop until incorrect answer is given
while not GAME_OVER:
    game()
