# Day9 for 100Days4Python
# Project for Day9

import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

auction = {}
more_bid = True

while more_bid:
    print("Welcome To The Auction")
    name = input("NAME : ")
    bid = int(input("BID : $"))
    auction[name] = bid
    if input("More Bidders? [Y/N] : ").lower() == "n":
        more_bid = False
    clear_console()

winner = ""
amount = 0
for bidder in auction:
    if amount < auction[bidder]:
        winner = bidder
        amount = auction[bidder]
print(auction)
print(f"The winner is {winner} with a bid of ${amount}")

