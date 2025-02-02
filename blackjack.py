import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

user_score = 0
dealer_score = 0

def random_card(player_cards, player_score, num_cards):

    for i in range(num_cards):
        player_cards.append(random.choice(cards))

    for i in range(len(player_cards)):
        player_score += player_cards[i]
  
    print(f"Your cards: {player_cards}, current score: {player_score}")

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':

    random_card(user_cards, user_score, 2)

