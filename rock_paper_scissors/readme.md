
# Rock, Paper, Scissors Game

## ✊✋🗞️ Description

The **Rock, Paper, Scissors Game** is a simple command-line game where the player competes against the computer. The player chooses one of three options (Rock, Paper, or Scissors), and the computer randomly selects one as well. The winner is determined based on the rules of the game:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

## 🧰 Key Concepts Covered

- Random Number Generation (`random` module)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while` loop)
- User Input and Output
- Function Definitions

## 🚀 How to Run the Game

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd rock_paper_scissors
Run the game:
bash
Copy code
python main.py
Follow the on-screen instructions to play the game.
📖 Gameplay Instructions

Upon running the game, you will be prompted to choose one of the three options:

Rock
Paper
Scissors
The computer will then make its selection, and the winner will be displayed.

Example Output:
markdown
Copy code
Welcome to Rock, Paper, Scissors!

Choose your option:
1. Rock
2. Paper
3. Scissors

Enter your choice (1-3): 1
You chose Rock. The computer chose Scissors.
You win!
🛠️ Code Overview

The application is structured with a main function and separate functions for game logic:

get_computer_choice(): Randomly selects the computer's choice.
determine_winner(player_choice, computer_choice): Determines the winner based on the player's and computer's choices.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this game, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Modular Functions

get_computer_choice(): Handles the logic for randomly selecting the computer's choice. It enhances readability and modularity.
determine_winner(player_choice, computer_choice): Contains the logic for determining the winner, making the main loop cleaner and focused on user interaction.
2. User Input Handling

Choice Validation: Checks if the player's input is a valid option (1-3). If not, it raises a ValueError, which is caught to provide feedback.
Loop for Replay: After each game, asks the player if they want to play again, creating a continuous gameplay experience.
3. Randomness

random.choice(): Uses the random module to select the computer's choice, demonstrating the use of randomness in games.
4. User Experience

Clear Prompts: Guides the player through the choices, ensuring they know how to interact with the game.
Feedback Messages: Displays the choices made by both the player and the computer, along with the result of the round.
5. Code Readability

Comments and Docstrings: Each function has a docstring that describes its purpose, improving maintainability.
Consistent Naming: Uses descriptive names for functions and variables.
6. Error Handling

Input Validation: Catches invalid input types and ranges, preventing crashes and providing a better user experience.
