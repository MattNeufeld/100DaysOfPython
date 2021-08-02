from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()

end = False

while not end:
    choices = menu.get_items()
    selection = input(f"What would you like today? ({choices}):")
    selection = selection.lower()
    if selection == "off":
        end = True
    elif selection == "report":
        cm.report()
        mm.report()
    else:
        drink = menu.find_drink(selection)
        ingredient = cm.is_resource_sufficient(drink)
        payment = mm.make_payment(drink.cost)
        if ingredient and payment:
            cm.make_coffee(drink)