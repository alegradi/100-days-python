# Tip Calculator
# If the bill was %150.00, split between 5 people, with 12% tip.
# Each person should pay ($150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

# What was the total bill?
# What percentage tip would you like to give? 10, 12 or 15?
# How many people to split the bill?
# Each person should pay: x.xx

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? £"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

per_person_cost = round((total_bill / number_of_people) * (1 + (tip_percentage / 100)), 2)

print("Each person should pay: £" + "%.2f" % round(per_person_cost, 2))  ## Rounded to 2 digits