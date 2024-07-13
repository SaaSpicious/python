from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

selection = "on"

while selection != "off":
    selection = input(f"What would you like to order? ({menu.get_items()}) ")
    if selection == "report":
        coffee_maker.report()
    elif selection == "off":
        print("Thank you for using the coffee machine.")
    elif menu.find_drink(selection) != None:
        drink = menu.find_drink(selection)
        print(f"You have ordered a {selection}!")
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

