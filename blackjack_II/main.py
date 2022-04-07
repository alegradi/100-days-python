# Blackjack
import random
import os
clear = lambda: os.system('clear')
#clear()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def deal_card():
    card = random.choice(cards)
    return card

cards_dealt = 0
while cards_dealt < 2:
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    cards_dealt += 1

print(f"user cards: {user_cards}")
print(f"computer cards: {computer_cards}")


def caclulate_score(hand):
    """
    Calculates the value of someone's hand
    Takes input of either user_cards or computer_cards
    """
    items_in_hand = len(hand)
    score = sum(hand)

    # Check if someone has Blackjack
    if items_in_hand == 2 and score == 21:
        score = 0
        print("Game over! Blackjack")
        game_over = True

    # Check if someone has 11 and gone over
    if score > 21:
        if 11 in hand:
            hand.remove(11)
            hand.append(1)

    # Check if the user has gone over
    if hand == user_cards and score > 21:
        print("Game Over! You have gone over!")
        game_over = True

    return score

game_over = False

print(caclulate_score(user_cards))


