import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

user_score = 0
computer_score = 0

# Generate random card
def random_card(player_cards, player_score, num_cards):

    for i in range(num_cards):
        player_cards.append(random.choice(cards))

    if num_cards > 1: # start: deals two cards
        for card in player_cards:
            player_score += card
    else: # deal one card
        player_score += player_cards[-1]

    return(player_score)
    
    

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':
    # Print user's two initial cards
    user_score = random_card(user_cards, user_score, 2)
    print(f"Your cards: {user_cards}, current score: {user_score}")

    # Print computer's first of two initial cards
    computer_score = random_card(computer_cards, computer_score, 2)
    print(f"Computer's first card: {computer_cards[0]}")

    # Ask user to get another card or to pass
    
    while True:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit == 'y':
            user_score = random_card(user_cards, user_score, 1)
            print(f"Your cards: {user_cards}, current score: {user_score}")

            computer_score = random_card(computer_cards, computer_score, 1)
            print(f"Computer's first card: {computer_cards[0]}")

        elif hit == 'n':
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    