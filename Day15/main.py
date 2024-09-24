# Day15 for 100Days4Python
# Project for Day15 : Coffee Machine 🍵

QRTR = 0.25 # quarters
DIME = 0.10 # dimes
NCKL = 0.05 # nickles
PNNY = 0.01 # pennies

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0

def get_order():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino" or order == "report":
        return order
    
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif order == "off":
        return False
    
    return get_order()

# TODO 3. Print report.
def resource_report():
  print(f"Water: {resources['water']}")
  print(f"Milk: {resources['milk']}")
  print(f"Coffee: {resources['coffee']}")
  print(f"Money: {money}")
  return True
  
# TODO 4. Check resources sufficient?
def resource_check(order):
    if resources["water"] >= MENU[order]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            if order != "espresso":
                if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                    return True
                return False
            return True
    return False

def transaction(order):
    # TODO 5. Process coins.
    quarters = int(input("Quarters: ")) * QRTR
    dimes =  int(input("Dimes: ")) * DIME
    nickles = int(input("Nickels: ")) * NCKL
    pennies = int(input("Pennies: ")) * PNNY
    change = quarters + dimes + nickles + pennies - MENU[order]["cost"]
    
    # TODO 6. Check transaction successful.
    if change >= 0:
        global money
        money += MENU[order]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 7. Make Coffee.
def make_coffee(order):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    if order != "espresso":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    print(f"Here is your {order}. Enjoy!")
    
# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): "
user_order = True
while user_order:
    user_order = get_order()
    if user_order == "report":
        resource_report()
    elif user_order and resource_check(user_order) and transaction(user_order):
        make_coffee(user_order)
