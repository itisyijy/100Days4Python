# Day16 for 100Days4Python
# Project for Day16 : OOP Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm_menu = Menu()
cm_coffeemaker = CoffeeMaker()
cm_moneymachine = MoneyMachine()
while True:
    cm_input = input(f"What would you like? ({cm_menu.get_items()}): ")
    if cm_input == "report":
        cm_coffeemaker.report()
        cm_moneymachine.report()
    elif cm_input == "off":
        break
    else:
        order = cm_menu.find_drink(cm_input)
        if order and cm_coffeemaker.is_resource_sufficient(order) and cm_moneymachine.make_payment(order.cost):
            cm_coffeemaker.make_coffee(order)