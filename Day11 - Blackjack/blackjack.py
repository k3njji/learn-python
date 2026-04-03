import random

def draw_card(hand):
    card = random.randint(1, 10)
    hand.append(card)
    return hand

def calculate_score(hand):
    total = sum(hand)
    ace_count = hand.count(1)
    while total <= 11 and ace_count > 0:
        total += 10
        ace_count -= 1
    return total

def calculate(player_hand, computer_hand):
    while calculate_score(computer_hand) < 17:
        computer_hand = draw_card(computer_hand)
    
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score {player_score}")
    print(f"Computer final hand: {computer_hand}, final score {computer_score}")

    if player_score > 21:
        print("You went over 21, you lose!")
        return False
    elif player_score > computer_score or computer_score > 21:
        print("Congratulations, you have won!")
        return True
    elif player_score < computer_score:
        print("You just lost!")
        return False
    else:
        print("This resulted in a draw!")
        return 'Draw'

def play_game():
    print("Welcome to Blackjack!")

    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if choice == 'n':
            print("Thank you for playing!")
            break

        player_hand = []
        computer_hand = []

        player_hand = draw_card(player_hand)
        player_hand = draw_card(player_hand)
        computer_hand = draw_card(computer_hand)

        while True:
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
            print(f"Computer's first card: {computer_hand[0]}")

            if calculate_score(player_hand) > 21:
                print("You went over 21, you lose!")
                break

            choice2 = input("Type 'y' to get another card, 'n' to pass: ").lower()

            if choice2 == 'n':
                result = calculate(player_hand, computer_hand)
                if result != 'Draw':
                    break
                else:
                    continue
            elif choice2 == 'y':
                draw_card(player_hand)
            else:
                print("Invalid input. Please type 'y' or 'n'.")
                continue

if __name__ == "__main__":
    play_game()