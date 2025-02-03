import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ////////////////////////////////////////////////////////////////// FUNCTIONS ////////////////////////////////////////////////////////////////////////

# INPUTS: user/pc cards, user/pc score, number of cards the they have
# FUNCTION: adds a random card to player's cards, updates their score
# RETURNS: score of player
def random_card(player_cards, player_score, num_cards):

    for card in range(num_cards):
        add_card = player_cards.append(random.choice(cards))
        if player_cards[-1] == 11 and player_score > 10: # if the player's score is over 10 and gets an ace, the ace will be given a value of 1
            player_cards[-1] = 1
            # print(f"Got an ace, but since player's score is above 10, the ace has been given a value of 1.")

    if num_cards > 1: # start: deals two cards
        for card in player_cards:
            player_score += card
    else: # hit: deal one card
        player_score += player_cards[-1]

    return(player_score)


# INPUTS: none
# FUNCTION: triggered if either or both players have score above 21. Both > 21 = both lose. Otherwise, player < 21 wins.
# RETURNS: none
def over_21():
    if user_score > 21 and computer_score > 21: # Both go over 21. Both lose
        display_scores()
        print("You both went over. Both lose.\n")
    elif user_score > 21: # User goes over 21 and loses
        display_scores()
        print("You went over. You lose.\n")
    elif computer_score > 21: # Computer goes over 21 and loses
        display_scores()
        print("Dealer went over. You win.\n")


# INPUTS: user score, computer score, hit or stand (bool)
# FUNCTION: checks if either or both players have a blackjack and assigns winner. If either score > 21, runs over_21() function to determine winner
# RETURNS: true if someone wins, so game_over can be set to it and terminate the game
def check_winner(user, computer, hit):
    # Above code block runs no matter if the user hits or stands to see if someone got a blackjack
    if user == 21 and computer == 21:
        display_scores()
        print("Tie!\n")
        return True
    elif user == 21:
        display_scores()
        print("You win!\n")
        return True
    elif computer == 21:
        display_scores()
        print("You lose.\n")
        return True
    elif user > 21 or computer > 21: # if either go over 21, game ends and both lose
        over_21()
        return True
    
    # Below code block only runs if user stands to see who has the higher score and determine winner
    if hit is False:
        if user > computer: # if user score > computer score, user wins
            display_scores()
            print("You win!\n")
            return True
        elif computer > user: # if computer score > user score, user loses
            display_scores()
            print("You lose.\n")
            return True
        elif user == computer:
            display_scores()
            print("Tie!\n")
            return True
    else:
        return False # if no one gets blackjack and hit is True, then it will return False, and game_over is set to False below to continue the game
    

# INPUTS: none
# FUNCTION: displays the user and computer's final cards and scores
# RETURNS: none
def display_scores():
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    

# ////////////////////////////////////////////////////////////////// CODE ////////////////////////////////////////////////////////////////////////

print(logo)

while True:
    # resets user and computer cards, scores, and game over status each round
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    game_over = False


    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'y':
        # Print user's two initial cards
        user_score = random_card(user_cards, user_score, 2)
        print(f"Your cards: {user_cards}, current score: {user_score}")

        # Print computer's first of two initial cards
        computer_score = random_card(computer_cards, computer_score, 2)
        print(f"Computer's first card: {computer_cards[0]}\n")
        # print(f"Computer's cards: {computer_cards}") # TEMPORARY: to show computers cards

        # Check if either player got a blackjack on first two cards
        game_over = check_winner(user_score, computer_score, True) # set hit == True so it doesn't trigger the latter half of check_winner() code (game ends b/c checks who has greater score)
        # print(f"Game over status: {game_over}\n")


        # Ask user to get another card or to pass
        while game_over is False: # if game_over from above returns True, then this section of the code will not run as the game as ended b/c a player got a blackjack
            hit = input("Type 'y' to get another card, type 'n' to pass: ")

            if hit == 'y':
                user_score = random_card(user_cards, user_score, 1)
                print(f"Your cards: {user_cards}, current score: {user_score}")

                # print(f"Computer's score: {computer_score}") # TEMPORARY: To show computer's score before they get another card

                if computer_score < 17: # Computer must hit if their score is 16 or below
                    computer_score = random_card(computer_cards, computer_score, 1)
                    
                print(f"Computer's first card: {computer_cards[0]}")
                # print(f"Computer's cards: {computer_cards}") # TEMPORARY: to show computers cards


                # Check if either or both players lost
                game_over = check_winner(user_score, computer_score, True)
                # print(f"Game over status: {game_over}\n")


            elif hit == 'n':
                game_over = check_winner(user_score, computer_score, False)
                # print(f"Game over status: {game_over}\n")
    