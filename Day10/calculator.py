# Day10 for 100Days4Python
# Project for Day10

import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def print_logo():
    print("""
      ___         ___         ___  ___         ___         ___  ___      ___         ___         ___     
     /\  \       /\  \       /\__\/\  \       /\__\       /\__\/\  \    /\  \       /\  \       /\  \    
    /::\  \     /::\  \     /:/  /::\  \     /:/  /      /:/  /::\  \   \:\  \     /::\  \     /::\  \   
   /:/\:\  \   /:/\:\  \   /:/  /:/\:\  \   /:/  /      /:/  /:/\:\  \   \:\  \   /:/\:\  \   /:/\:\  \  
  /:/  \:\  \ /::\~\:\  \ /:/  /:/  \:\  \ /:/  /  ___ /:/  /::\~\:\  \  /::\  \ /:/  \:\  \ /::\~\:\  \ 
 /:/__/ \:\__/:/\:\ \:\__/:/__/:/__/ \:\__/:/__/  /\__/:/__/:/\:\ \:\__\/:/\:\__/:/__/ \:\__/:/\:\ \:\__\\
 \:\  \  \/__\/__\:\/:/  \:\  \:\  \  \/__\:\  \ /:/  \:\  \/__\:\/:/  /:/  \/__\:\  \ /:/  \/_|::\/:/  /
  \:\  \          \::/  / \:\  \:\  \      \:\  /:/  / \:\  \   \::/  /:/  /     \:\  /:/  /   |:|::/  / 
   \:\  \         /:/  /   \:\  \:\  \      \:\/:/  /   \:\  \  /:/  /\/__/       \:\/:/  /    |:|\/__/  
    \:\__\       /:/  /     \:\__\:\__\      \::/  /     \:\__\/:/  /              \::/  /     |:|  |    
     \/__/       \/__/       \/__/\/__/       \/__/       \/__/\/__/                \/__/       \|__|    
""")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}   # dictionary value for function name!!!

def print_operators():
    for symbol in operations:
        print(f"[{symbol}] ", end="")
    print()

def calculate():
    print_logo()
    a = float(input("FIRST NUMBER >>> "))
    while True:
        print_operators()
        operator = input("PICK AN OPERATION >>> ")
        b = float(input("NEXT  NUMBER >>> "))
        result = operations[operator](a, b)
        print(f"{a} {operator} {b} = {result}")
        if input(f"[y] for continue calculating with {result} | [n] for start new calculation : ").lower() == "n":
            break
        a = result
    clear_console()
    calculate()

calculate()