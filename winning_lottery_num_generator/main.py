# Generate the winning lottery numbers for EuroMillions
# 5 numbers from 1 - 50
# 2 numbers from 1 - 12 

import random

from requests import get

primary_number_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secondary_number_pool = [1, 2, 3, 4]

primary_winning_numbers = []
secondary_winning_numbers = []

# Get a random number from a list and remove it
def get_number(list_name):
    winning_number = random.choice(list_name)
    print(winning_number)
    list_name.remove(winning_number)
    # print(list_name)

get_number(primary_number_pool)
