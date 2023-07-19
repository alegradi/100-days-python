# Coffee Machine
from data import MENU

# Global variables
MACHINE_OFF = False


def main_loop():
    """
    Main program loop. Waiting for user input.
    Exit by typing 'off'
    """
    global MACHINE_OFF

    choice = str(input("What would you like? (espresso/latte/cappuccino): ").lower())

    if choice == 'off':
        MACHINE_OFF = True
        return
    elif choice == 'report':
        print("Printing report")
        return_resources()
    else:
        check_resources(choice)

    # After a loop return the resources, Debug info
    # return_resources()


def return_resources():
    """
    Return resources.
    """
    resource_water = resources['water']
    resource_milk = resources['milk']
    resource_coffee = resources['coffee']
    print(f"Water: {resource_water}ml")
    print(f"Milk: {resource_milk}ml")
    print(f"Coffee: {resource_coffee}g")
    print(f"Money: ${profit}")


def check_resources(request):
    """
    Checks if we have enough resources to produce the requested item
    """
    if request == 'espresso':
        if resources['water'] < MENU[request]['ingredients']['water']:
            print("Sorry, there isn't enough water!")
            return
        elif resources['coffee'] < MENU[request]['ingredients']['coffee']:
            print("Sorry, there isn't enough coffee!")
            return
    else:
        if resources['milk'] < MENU[request]['ingredients']['milk']:
            print("Sorry, there isn't enough milk!")
            return

    print("All resource requirements have been met. Continuing - Debug info")
    inserted_money = process_coins()

    transaction(request, inserted_money)


def process_coins():
    """
    Processing coins.
    Returns the sum of inserted coins
    """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    # Sum up the money
    inserted_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return inserted_money


def transaction(drink_option, inserted_money):
    global resources, profit
    """
    Verify if the user inserted enough money
    Proceed to making a drink if yes
    Tell when they didn't
    Give change back if money is too much
    """
    if inserted_money < MENU[drink_option]['cost']:
        print("Not enough money has been inserted")
        return
    else:
        change = inserted_money - MENU[drink_option]['cost']
        # '{0:.2f}'.format(change) # doesn't work for some reason
        if change > 0:
            print(f"Your change is: ${change}")
    # Reduce the amount of resources by what has been ordered
    resources['water'] = resources['water'] - MENU[drink_option]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[drink_option]['ingredients']['coffee']
    if drink_option != 'espresso':
        resources['milk'] = resources['milk'] - MENU[drink_option]['ingredients']['milk']
    # Add the money to the machine
    profit = profit + MENU[drink_option]['cost']

    print("\nHere's your drink!\n")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

while not MACHINE_OFF:
    main_loop()


