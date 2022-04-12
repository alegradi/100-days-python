# Blackjack
import random
import os
clear = lambda: os.system('clear')
#clear()

def deal_card():
    """
    Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Check if Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Check if gone over and one of the cards is an Ace (11)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(score1, score2):
    """
    Compares the user_score and computer_score
    """
    if score1 == score2:
        print("\nThis is a draw!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score1 == 0:
        print("\nUser has Blackjack!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score2 == 0:
        print("\nComputer has Blackjack!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score1 > 21:
        print("\nYou have gone over, Computer wins!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score2 > 21:
        print("\nComputer has gone over, player wins!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score1 > score2:
        print("\nPlayer wins with higher card value!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    elif score1 < score2:
        print("\nComputer wins with higher card value!")
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")

continue_game = "y"

while continue_game == "y":
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal 2 cards to both computer and player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)

    continue_game = input("\nWould you like to play another game? Type 'y' for yes: ")
    clear()
