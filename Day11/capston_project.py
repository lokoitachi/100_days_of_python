from art import logo
from random import choice
from clear import clear

def deal_card():
    """Returns a random cards from a deck list given by default"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def calculate_score(cards):
    """This function will take a list of cards and return the score calculated from the cards"""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    
    return score

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    user_deck = []
    computer_deck = []
    is_game_over = False


    print(logo)
    for _ in range(2):
        user_deck.append(deal_card())
        computer_deck.append(deal_card( ))

    while not is_game_over: 
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your current cards are:{user_deck}. Your current score is {user_score}")
        print(f"The computer first card would be: {computer_deck[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_wants_another_card = input("Do you want to draw another card? Type 'y' if you want. Otherwise type 'n'")
            if user_wants_another_card.lower() == "y":
                user_deck.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_deck.append(deal_card())
        computer_score = calculate_score(computer_deck)

    print(f"You deck is now: {user_deck} and your score is: {user_score}")
    print(f"Computer deck is: {computer_deck} and its score is: {computer_score}")


    compare(user_score=user_score, computer_score=computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' if you want to. Otherwise type 'n'").lower() == 'y':

    clear()
    play_game()
    




    


    


