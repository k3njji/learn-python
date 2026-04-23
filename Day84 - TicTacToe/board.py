class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]

    def display(self):
        print("\nBoard:")
        for row in self.board:
            print(' | '.join(row))
        print()

    def addBoard(self, player, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Out of Bound Bro')
            return False

        if self.board[row][col] != '_':
            print('Cell already taken')
            return False

        self.board[row][col] = player.mark
        return self.check(row, col, player)

    def check(self, row, col, player):
        mark = player.mark

        if all(self.board[row][c] == mark for c in range(3)):
            return True

        if all(self.board[r][col] == mark for r in range(3)):
            return True

        if row == col:
            if all(self.board[i][i] == mark for i in range(3)):
                return True

        if row + col == 2:
            if all(self.board[i][2 - i] == mark for i in range(3)):
                return True

        return False

    def is_full(self):
        return all(self.board[r][c] != '_' for r in range(3) for c in range(3))