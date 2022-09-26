# Generate the winning lottery numbers for EuroMillions
# 5 numbers from 1 - 50
# 2 numbers from 1 - 12 

import random
from requests import get

primary_number_pool = []
secondary_number_pool = []

for _ in range(1,13,1):
    secondary_number_pool.append(str(_))

for _ in range(1,51,1):
    primary_number_pool.append(str(_))


# Debug info
# print(f"Primary pool is: {primary_number_pool}")
# print(f"Secondary pool is: {secondary_number_pool}")

primary_winning_numbers = []
secondary_winning_numbers = []


def get_numbers(list_name, output_list):
    global primary_winning_numbers
    global secondary_winning_numbers

    winning_number = random.choice(list_name)
    list_name.remove(winning_number)
    output_list.append(winning_number)

    # Debug info
    # print(f"\nCurrent list is:", list_name)
    # print(f"Current number selected:", winning_number)
    # print(f"Selected number list:", output_list)


# Get the first 5 numbers
while len(primary_winning_numbers) < 5:
    get_numbers(primary_number_pool, primary_winning_numbers)

# Get the second 2 numbers
while len(secondary_winning_numbers) < 2:
    get_numbers(secondary_number_pool, secondary_winning_numbers)

print(f"Your primary numbers are: ", primary_winning_numbers)
print(f"Your secondary numbers are: ", secondary_winning_numbers)