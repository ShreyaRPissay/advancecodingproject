def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row, col = map(int, input(f"Player {players[player_idx]}, enter your move (row col): ").split())

        if board[row][col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[row][col] = players[player_idx]
        print_board(board)

        if check_winner(board, players[player_idx]):
            print(f"Player {players[player_idx]} wins!")
            return

        player_idx = (player_idx + 1) % 2

    print("It's a tie!")
tic_tac_toe()
