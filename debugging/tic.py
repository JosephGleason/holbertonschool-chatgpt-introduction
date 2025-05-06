#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")  # matches the 3×3 layout
    print()  # extra newline for readability

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True
    # Check columns
    for col in range(3):
        if (board[0][col] != " " and
            board[0][col] == board[1][col] == board[2][col]):
            return True
    # Check diagonals
    if (board[1][1] != " " and
        ((board[0][0] == board[1][1] == board[2][2]) or
         (board[0][2] == board[1][1] == board[2][0]))):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # --- get a valid row ---
        while True:
            try:
                row = int(input(f"Enter row (0,1,2) for {player}: "))
                if row in (0,1,2):
                    break
            except ValueError:
                pass
            print("Invalid row. Please enter 0, 1, or 2.")

        # --- get a valid column ---
        while True:
            try:
                col = int(input(f"Enter column (0,1,2) for {player}: "))
                if col in (0,1,2):
                    break
            except ValueError:
                pass
            print("Invalid column. Please enter 0, 1, or 2.")

        # --- check occupancy ---
        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        # --- place the move ---
        board[row][col] = player

        # --- check for a win ---
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # --- check for a draw ---
        if all(cell != " " for r in board for cell in r):
            print_board(board)
            print("It's a draw!")
            break

        # --- switch turns ---
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
