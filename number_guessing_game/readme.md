README.md
markdown
Copy code
# Number Guessing Game

## 🎯 Description

Welcome to the **Number Guessing Game**! In this interactive command-line game, the computer randomly selects a number between 1 and 100. Your task is to guess the number with the help of hints provided after each guess.

## 🧰 Key Concepts Covered

- Variables and Data Types
- Loops (`while` loop)
- Conditional Statements (`if`, `elif`, `else`)
- User Input (`input()` function)
- Exception Handling (`try`, `except`)
- Random Number Generation (`random` module)
- Functions and Code Organization

## 🚀 How to Run the Game

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd number_guessing_game
Run the game:
bash
Copy code
python main.py
Follow the on-screen instructions to play the game.
🎮 Gameplay Instructions

Objective: Guess the number the computer has selected.
Input: Enter your guess when prompted.
Feedback:
"Too low!": Your guess is less than the number.
"Too high!": Your guess is greater than the number.
"Congratulations!": You guessed the correct number.
Play Again: After the game ends, you will be prompted to play again.
📄 Sample Output

vbnet
Copy code
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 40
Too low! Try again.

Enter your guess: 70
Too high! Try again.

Enter your guess: 60
Too high! Try again.

Enter your guess:  Fifty
Invalid input. Please enter an integer between 1 and 100.

Enter your guess: 55
Congratulations! You guessed the number in 5 tries!

Do you want to play again? (yes/no): no
Thank you for playing!
🛠️ Code Overview

The program is divided into functions for better organization:

play_number_guessing_game(): Contains the main game logic.
main(): Manages game sessions and replay functionality.
Modules Used
random: For generating a random number.
sys: For system-specific parameters and functions (not used in this version but good to know for future enhancements).
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this game, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

Code Explanation and Best Practices
Function Definitions: The game logic is encapsulated within functions (play_number_guessing_game and main) for better modularity and readability.
Random Number Generation: Utilizes random.randint(1, 100) to generate a random number inclusive of both endpoints.
User Input Handling:
Input Validation: Checks if the input is an integer and within the valid range (1-100).
Exception Handling: Uses try and except blocks to catch ValueError exceptions when the user inputs non-integer values.
Loop Control:
Game Loop: Uses a while True loop to continue prompting the user until the correct number is guessed.
Replay Option: After the game ends, the user is asked if they want to play again.
User Feedback:
Provides clear and immediate feedback after each guess.
Encourages the user by keeping track of the number of attempts.
Code Comments: Includes docstrings and comments for better understanding and maintainability.
Tips for Beginners
Readability: Write code that is easy to read and understand. Use meaningful variable and function names.
Testing: Test your code with various inputs, including edge cases like invalid inputs or numbers outside the expected range.
Error Handling: Always anticipate possible errors and handle them gracefully to improve user experience.
Code Organization: Organize your code into functions to make it modular and reusable.
