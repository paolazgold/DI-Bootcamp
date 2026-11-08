
#Step 1: Representing the Game Board
"""You’ll need a way to represent the 3x3 grid.
A list of lists (a 2D list) is a good choice.
Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘)."""

board_game = [[ ' ', ' ', ' '], [ ' ', ' ', ' '],[ ' ', ' ', ' ']]

#Step2: Displaying the Game Board
"""Create a function called display_board() to print the current state of the game board.
The output should visually represent the 3x3 grid.
Think about how to format the output to make it easy to read."""

def display_board():
    for i in range(len(board_game)):
        for cell in board_game[i]:
            print('', cell, end=' | ')
        print()

        if i < len(board_game) - 1:
            print("------------")

#Step 3:Getting Player Input

def player_input(player):
    row = int(input("Choose a row (1-3): ")) - 1
    column = int(input("Choose a column (1-3): ")) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:
        print("This position does not exist!")

    elif board_game[row][column] == ' ':
        board_game[row][column] = player

    else:
        print("This position is already occupied!")

    display_board()

#Step 4: Step 4: Checking for a Winner

"""Create a function called check_win(board, player) to check if the current player has won.
The function should check all possible winning combinations (rows, columns, diagonals).
If a player has won, return True; otherwise, return False.
Think about how to check every possible winning combination."""

def check_win(board, player):

    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    # Check first diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # Check second diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

#Step 5 Checking for a Tie

"""Create a function to check if the game has resulted in a tie.
The function should check if all positions of the board are full, without a winner."""

def check_tie(board):

    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    if not check_win(board, 'X') and not check_win(board, 'O'):
        return True

    return False

    #Step 6

    def play():

    current_player = 'X'
    game_over = False

    while not game_over:

        # Display the board
        display_board()

        # Get player's input
        player_input(current_player)

        # Check if the current player won
        if check_win(board_game, current_player):
            display_board()
            print(f"Player {current_player} wins!")
            game_over = True

        # Check if the game is a tie
        elif check_tie(board_game):
            display_board()
            print("It's a tie!")
            game_over = True

        # Switch player
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'


play()



