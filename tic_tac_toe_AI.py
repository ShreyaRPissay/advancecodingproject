import random
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)
def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True
def ai_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_win(board, player):
                    return i, j
                board[i][j] = ' '
    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent
                if check_win(board, opponent):
                    board[i][j] = player
                    return i, j
                board[i][j] = ' '
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    player = 'X'
    while True:
        if player == 'X':
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] != ' ':
                print("That cell is already occupied. Try again.")
                continue
            board[row][col] = player
        else:
            print("AI's turn:")
            row, col = ai_move(board, player)
            board[row][col] = player
        print_board(board)
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'
play_game()
