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

print(auction)

#1 get key with max value in dictionary
winner = ""
amount = 0
for bidder in auction:
    if amount < auction[bidder]:
        winner = bidder
        amount = auction[bidder]
print(f"[FOR] The winner is {winner} with a bid of ${amount}")

#2 get key with max value in dictionary
winner = max(auction, key=auction.get)
amount = max(auction.values())
print(f"[MAX] The winner is {winner} with a bid of ${amount}")