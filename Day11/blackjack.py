# Day11 for 100Days4Python
# Project for Day11
import os
import random

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def print_blackjack():
    print("""
$$$$$$$\  $$\        $$$$$$\   $$$$$$\  $$\   $$\   $$$$$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$ | $$  |  \__$$ |$$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|$$ |$$  /      $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$\ |$$ |      $$$$$$$$ |$$ |      $$$$$  /       $$ |$$$$$$$$ |$$ |      $$$$$  /  
$$  __$$\ $$ |      $$  __$$ |$$ |      $$  $$<  $$\   $$ |$$  __$$ |$$ |      $$  $$<   
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\ $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$$$$$$  |$$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ | \$$\\$$$$$$  |$$ |  $$ |\$$$$$$  |$$ | \$$\ 
\_______/ \________|\__|  \__| \______/ \__|  \__|\______/ \__|  \__| \______/ \__|  \__|
""", end="")

def hit_or_stand():
    """
    Player can select their action : HIT / STAND

    :return:
    HIT = 1\n
    STAND = 0
    """
    hit = int(input("HIT [1] or STAND [0] >>> "))
    if hit:
        print("You Chose HIT")
    else:
        print("You Chose STAND")
    return hit

def hit_card(hand, deck, count):
    """
    Each player can hit number of cards from deck\n
    hit cards are removed from the deck

    :param hand: player's cards on their hand
    :param deck: left card deck
    :param count: number of cards player want to hit
    """
    hand.extend(random.sample(deck, count))
    deck.remove(hand[-1])

def init_game(player1, player2, deck):
    """
    Start the Blackjack.\n
    Each player get 2 cards from the deck one by one.

    :param player1: who get a card first
    :param player2: who get a card last
    :param deck: card deck
    """
    hit_card(player1, deck, 1)
    hit_card(player2, deck, 1)
    hit_card(player1, deck, 1)
    hit_card(player2, deck, 1)

def hand_sum(hand):
    """
    return sum of cards in hand

    :param hand: hand which you wonder its total
    :return: sum of total cards from the hand
    """
    result = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            result += 10
        elif card == 'A' and  result >= 11:
                result += 1
        elif card == 'A' and result < 11:
                result += 11
        else:
            result += int(card)
    return result

def bust_check(hand):
    """
    check the hand is bust or not

    :param hand: wondering bust or not
    :return: BUST = 1 / Blackjack = -1 / Nothing = 0
    """
    if hand_sum(hand) > 21:     # Bust
        return 1
    elif hand_sum(hand) == 21:  # Blackjack
        return -1
    else:                       # Ongoing
        return 0

def judge(dealer, player):
    """
    judge who is winner

    :param dealer:
    :param player:
    """
    if bust_check(dealer) == 1:
        print("!! House BUST !!")
    elif bust_check(player) == 1:
        print("!! Player BUST !!")
    elif hand_sum(player) == 21:
        print("!! Player Blackjack !!")
    elif hand_sum(dealer) == 21:
        print("!! Dealer Blackjack !!")
    elif hand_sum(dealer) > hand_sum(player):
        print("!! House Win !!")
    elif hand_sum(dealer) < hand_sum(player):
        print("!! Player Win !!")
    else:
        print("!! PUSH !!")

def show_hands(dealer, player, option):
    """
    show each hand of dealer and player

    :param dealer:
    :param player:
    :param option: hide dealer's second card = 1 / show all cards = 0
    """
    print("\n------------------------------------")
    if option:
        print(f"DEALER : ['{dealer[0]}', '?'] >>> {hand_sum([dealer[0]])}")
    else:
        print(f"DEALER : {dealer} >>> {hand_sum(dealer)}")
    print(f"PLAYER : {player} >>> {hand_sum(player)}")
    print("------------------------------------\n")