# Day11 for 100Days4Python
# Project for Day11

import blackjack

replay = True
while replay:
    blackjack.clear_console()
    blackjack.print_blackjack()
    deck = (['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4) * 1
    dealer = []
    player = []

    # 1 - Initial Deal
    blackjack.start_game(dealer, player, deck)
    blackjack.show_hands(dealer, player, 1)

    if blackjack.hand_sum(player) != 21: # Player is not blackjack. Keep going.
        # 2 - Player's Turn : Hit Or Stand
        hit = blackjack.hit_or_stand()
        while hit and blackjack.bust_check(player) != -1:
            blackjack.deal_card(player, deck, 1)
            blackjack.show_hands(dealer, player, 1)
            if blackjack.bust_check(player): # Player is bust. Check the result
                blackjack.show_hands(dealer, player, 0)
                break
            hit = blackjack.hit_or_stand()

        # 3 - Dealer's Turn
        if not blackjack.bust_check(player):
            blackjack.show_hands(dealer, player, 0)
            while blackjack.hand_sum(dealer) <= 16:
                blackjack.deal_card(dealer, deck, 1)
                blackjack.show_hands(dealer, player, 0)
    else:
        blackjack.show_hands(dealer, player, 0)
    blackjack.judge(dealer, player)
    replay = int(input("\nREPLAY [1] or END [0] >>> "))