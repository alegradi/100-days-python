# OOP coffee machine
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

machine_on = True

while machine_on:
    user_choice = input("What would you like? (" + menu.get_items() + "): ")
    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        menuitem = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(menuitem):
            if moneymachine.make_payment(menuitem.cost):
                coffeemaker.make_coffee(menuitem)
