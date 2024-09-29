# Hangman Game

## 🎯 Description

The **Hangman Game** is a classic word-guessing game where the player attempts to guess a secret word one letter at a time. The player has a limited number of attempts to guess the word correctly before the game is over.

## 🧰 Key Concepts Covered

- String Manipulation
- Lists and Data Structures
- Loops (`while` and `for` loops)
- Conditional Statements (`if`, `elif`, `else`)
- Functions and Modular Code
- Randomness (`random` module)
- User Input and Output

## 🚀 How to Play the Hangman Game

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd hangman_game
Run the game:
bash
Copy code
python main.py
Follow the on-screen instructions to guess the secret word.
📖 Gameplay Instructions

A random word is selected from a predefined list.
The word is represented by a series of underscores _, indicating unguessed letters.
You guess one letter at a time.
If the guessed letter is in the word, it is revealed in its correct position(s).
If the guessed letter is not in the word, you lose one attempt.
The game continues until you guess the word or run out of attempts.
Example Output:
python
Copy code
Welcome to Hangman!

Word to guess: _ _ _ _ _

Attempts remaining: 6
Guessed letters: 

Enter a letter: e
Good guess!

Word to guess: _ e _ _ _

Attempts remaining: 6
Guessed letters: e

Enter a letter: a
Sorry, 'a' is not in the word.

Word to guess: _ e _ _ _
Attempts remaining: 5
Guessed letters: e, a

... (game continues)

Congratulations! You've guessed the word 'hello'!
🛠️ Code Overview

The application is structured with functions to handle different parts of the game:

get_random_word(word_list): Selects a random word from the list.
display_current_progress(word, guessed_letters): Displays the word with guessed letters revealed.
play_hangman(word): Manages the game loop and logic.
main(): Initializes the game.
Modules Used
random: For selecting a random word from the list.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this Hangman game, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

## Code Explanation and Best Practices
1. Modular Functions

get_random_word(word_list): Selects a random word from the provided list, making it easy to manage and update the word bank.
display_current_progress(word, guessed_letters): Builds a string representation of the current progress, showing guessed letters and underscores.
play_hangman(word): Contains the main game loop, handling user input and game logic.
main(): Sets up the game by initializing the word list and starting the game.
2. Data Structures

Lists and Sets: Uses lists to store guessed letters and sets for efficient lookup of word letters.
3. User Input Handling

Input Validation: Ensures the user inputs a single alphabetical character.
Duplicate Guesses: Checks if the letter has already been guessed.
4. Game Logic

Attempts Tracking: Decreases the number of attempts remaining when a wrong guess is made.
Win/Loss Conditions: Determines if the player has won or lost based on guessed letters and attempts remaining.
5. User Experience

Clear Display: Shows the current progress of the word, attempts remaining, and guessed letters.
Feedback Messages: Provides immediate feedback on the guess (correct, incorrect, invalid input).
6. Code Readability

Comments and Docstrings: Each function includes a docstring explaining its purpose.
Consistent Naming: Uses descriptive variable and function names.
Whitespace and Formatting: Follows PEP 8 style guidelines for readability.