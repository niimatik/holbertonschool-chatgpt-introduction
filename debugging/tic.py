#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board with visual separators.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--+---+--")

def check_winner(board):
    """
    Checks for a winning condition: rows, columns, and diagonals.
    Returns the winning player's symbol ('X' or 'O') if there's a winner, else None.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Returns True if all cells are filled; otherwise, False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a game of Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of bounds. Please enter values between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
