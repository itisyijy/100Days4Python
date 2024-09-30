# Day16 for 100Days4Python
# Project for Day16 : OOP Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm_menu = Menu()
cm_coffee_maker = CoffeeMaker()
cm_money_machine = MoneyMachine()

while True:
    cm_input = input(f"What would you like? ({cm_menu.get_items()}): ")
    if cm_input == "report":
        cm_coffee_maker.report()
        cm_money_machine.report()
    elif cm_input == "off":
        break
    else:
        cm_order = cm_menu.find_drink(cm_input)
        if cm_order:
            if cm_coffee_maker.is_resource_sufficient(cm_order):
                if cm_money_machine.make_payment(cm_order.cost):
                    cm_coffee_maker.make_coffee(cm_order)