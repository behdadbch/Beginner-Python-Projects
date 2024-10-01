# Tic-Tac-Toe Game

## 🎮 Description

The **Tic-Tac-Toe Game** is a command-line implementation of the classic two-player game. Players take turns placing their marks (X or O) on a 3x3 grid. The first player to align three of their marks horizontally, vertically, or diagonally wins the game. If all nine squares are filled without a winner, the game ends in a draw.

## 🧰 Key Concepts Covered

- Data Structures (lists, dictionaries)
- Functions and Modular Code
- Control Flow (loops, conditionals)
- User Input and Output
- Game Logic Implementation

## 🚀 How to Play the Tic-Tac-Toe Game

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd tic_tac_toe
Run the game:
bash
Copy code
python main.py
Follow the on-screen instructions to play the game.
📖 Gameplay Instructions

The game is played on a 3x3 grid numbered from 1 to 9:
markdown
Copy code
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
Player 1 is assigned the mark X, and Player 2 is assigned the mark O.
Players take turns entering the number corresponding to the cell where they want to place their mark.
The game checks for a winner after each move.
If all cells are filled without a winner, the game ends in a draw.
Example Output:
markdown
Copy code
Welcome to Tic-Tac-Toe!

Player 1 (X)  -  Player 2 (O)

Current Board:
   |   |   
-----------
   |   |   
-----------
   |   |   

Player 1, choose your move (1-9): 5

Current Board:
   |   |   
-----------
   | X |   
-----------
   |   |   

Player 2, choose your move (1-9): 1

Current Board:
 O |   |   
-----------
   | X |   
-----------
   |   |   

... (game continues)

Player 1 wins! Congratulations!
🛠️ Code Overview

The application is structured with functions to handle different parts of the game:

display_board(board): Displays the current state of the game board.
player_input(player, board): Handles input from the current player.
check_win(board, mark): Checks if a player has won.
check_draw(board): Checks if the game is a draw.
main(): Manages the game loop and overall flow.
Modules Used
No external modules are required.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this Tic-Tac-Toe game, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Modular Functions

display_board(board): Responsible for displaying the game board in its current state.
player_input(player, board): Handles the input from the current player and updates the board accordingly.
check_win(board, mark): Checks all possible winning combinations to determine if a player has won.
check_draw(board): Determines if the game has ended in a draw.
main(): Manages the overall game flow, including initializing the board, switching players, and handling replay.
2. Data Structures

Dictionary: The board is represented as a dictionary with keys '1' to '9', corresponding to each position on the board.
3. Game Logic

Winning Conditions: Checks all possible lines (rows, columns, diagonals) for a win.
Player Switching: Alternates between Player 1 ('X') and Player 2 ('O').
4. User Input Handling

Input Validation: Ensures that the player selects a valid, unoccupied position.
Replay Option: Allows players to choose whether to play another game after one concludes.
5. User Experience

Clear Display: Provides a visual representation of the board after each move.
Feedback Messages: Informs players of invalid moves, wins, draws, and game status.
6. Code Readability

Comments and Docstrings: Functions include docstrings explaining their purpose.
Consistent Naming: Uses descriptive variable and function names.
Formatting: Follows PEP 8 style guidelines for readability.
Enhancements and Extensions
Consider adding the following features to enhance the Tic-Tac-Toe game:

Input Enhancement: Allow players to enter positions using row and column numbers.
AI Opponent: Implement a basic AI for single-player mode.
Improved Interface: Enhance the visual display with better formatting or ASCII art.
Score Tracking: Keep track of wins, losses, and draws over multiple games.
Testing the Tic-Tac-Toe Game
Valid Moves: Ensure that valid moves are accepted and reflected on the board.
Invalid Moves: Test selecting occupied positions or invalid numbers to verify input validation.
Win Conditions: Play through games to test all possible winning scenarios.
Draw Condition: Confirm that the game correctly identifies a draw when all positions are filled without a winner.
Replay Functionality: Test the option to play multiple games in a session.