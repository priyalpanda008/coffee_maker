from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
Money_machine = MoneyMachine()
menu = Menu()


is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and Money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)










