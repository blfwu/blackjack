import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

user_score = 0
computer_score = 0

def random_card(player_cards, player_score, num_cards):

    for i in range(num_cards):
        player_cards.append(random.choice(cards))

    for card in player_cards:
        player_score += card

    return(player_score)
    
    

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':
    # Print player's two initial cards
    user_score = random_card(user_cards, user_score, 2)
    print(f"Your cards: {user_cards}, current score: {user_score}")

    # Print computer's first of two initial cards
    random_card(computer_cards, computer_score, 2)
    print(f"Computer's first card: {computer_cards[0]}")