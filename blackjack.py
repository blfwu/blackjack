import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

player_score = 0
dealer_score = 0


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':
    # PLAYER
    player_cards.extend([random.choice(cards), random.choice(cards)])
    player_score = player_cards[0] + player_cards[1]
    print(f"Your cards: {player_cards}, current score: {player_score}")

    # COMPUTER
