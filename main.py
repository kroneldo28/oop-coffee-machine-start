from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
bank = MoneyMachine()
machine_on = True
money_in_the_machine = 0

while machine_on:
    # Get the user choice
    choice = input("\nWhat would you like? [Espresso($1.5), Latte($2.5), Cappuccino($3.0)? ").lower()
    if choice == "off":
        print("The machine is turned off. Good bye!")
        machine_on = False
    elif choice == "report":
        machine.report()
        bank.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            print(f"You chose {choice}")
            # We check if the resources are sufficient
            if machine.is_resource_sufficient(drink):
                if bank.make_payment(drink.cost):
                    machine.make_coffee(drink)
