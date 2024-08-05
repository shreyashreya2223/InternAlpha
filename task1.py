import random

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if (0 <= row <= 2 and 0 <= col <= 2) and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")

def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def play_game(single_player):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == 'X' or not single_player:
            print(f"Player {current_player}'s turn")
            row, col = get_player_move(board)
        else:
            print("Computer's turn")
            row, col = get_computer_move(board)

        # Make the move
        board[row][col] = current_player

        # Check for win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!\n")
    while True:
        mode = input("Do you want to play one player or two players? (1/2): ").strip()
        if mode == '1':
            single_player = True
        elif mode == '2':
            single_player = False
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        play_game(single_player)
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()