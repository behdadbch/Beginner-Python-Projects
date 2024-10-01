
def display_board(board):
    """
    Displays the current state of the game board.
    """
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("---|---|---")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("---|---|---")
    print(f" {board['7']} | {board['8']} | {board['9']} ")

def player_input(player, board):
    """
    Prompts the current player to choose a position on the board.
    """
    while True:
        choice = input(f"\nPlayer {player}, choose your move (1-9): ").strip()
        if choice in board and board[choice] == ' ':
            board[choice] = player
            break
        else:
            print("Invalid move. Please try again.")

def check_win(board, mark):
    """
    Checks if the given mark has won the game.
    """
    win_conditions = [
        ['1', '2', '3'],  # Top row
        ['4', '5', '6'],  # Middle row
        ['7', '8', '9'],  # Bottom row
        ['1', '4', '7'],  # Left column
        ['2', '5', '8'],  # Middle column
        ['3', '6', '9'],  # Right column
        ['1', '5', '9'],  # Diagonal from top-left
        ['3', '5', '7']   # Diagonal from top-right
    ]
    for condition in win_conditions:
        if all(board[pos] == mark for pos in condition):
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw.
    """
    return all(space != ' ' for space in board.values())

def main():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    print("Welcome to Tic-Tac-Toe!\n")
    print("Player 1 (X)  -  Player 2 (O)\n")

    while True:
        board = {str(num): ' ' for num in range(1, 10)}
        current_player = 'X'

        while True:
            print("\nCurrent Board:")
            display_board(board)
            player_input(current_player, board)

            if check_win(board, current_player):
                print("\nCurrent Board:")
                display_board(board)
                print(f"\nPlayer {current_player} wins! Congratulations!")
                break

            if check_draw(board):
                print("\nCurrent Board:")
                display_board(board)
                print("\nIt's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing Tic-Tac-Toe! Goodbye!")
            break

if __name__ == "__main__":
    main()
