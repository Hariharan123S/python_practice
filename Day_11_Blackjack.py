import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score > 21:
        return "You went over.You lose"
    elif c_score > 21:
        return "Opponent went over.You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    print(art.logo_blackjack)
    user = []
    computer = []
    computer_score = -1
    is_game_over = False

    for i in range(2):
        user.append(deal_cards())
        computer.append(deal_cards())


    while not is_game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_game == "y":
                user.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 21:
        computer.append(deal_cards())
        computer_score = calculate_score(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a new game of Black jack? Type 'y' or 'n': "):
    print("\n" * 20)
    play_game()
