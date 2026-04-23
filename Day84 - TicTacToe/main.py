from player import Player
from board import TicTacToe

game = TicTacToe()
p1 = Player('X')
p2 = Player('O')

players = [p1, p2]
turn = 0

while True:
    current = players[turn % 2]

    game.display()
    print(f"Player {current.mark}'s turn")

    try:
        row = int(input("Row (0-2): "))
        col = int(input("Col (0-2): "))
    except:
        print("Invalid input, use numbers 0-2")
        continue

    result = game.addBoard(current, row, col)

    if result:
        game.display()
        print(f"Player {current.mark} wins!")
        current.addScore()

        print(f"Score: X={p1.score}, O={p2.score}")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

        game.reset()
        turn = 0
        continue

    if game.is_full():
        game.display()
        print("Draw!")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

        game.reset()
        turn = 0
        continue

    turn += 1