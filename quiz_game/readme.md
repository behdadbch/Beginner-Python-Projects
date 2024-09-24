# Simple Quiz Game

## 🧠 Description

The **Simple Quiz Game** is a command-line application where users answer multiple-choice questions. At the end of the quiz, the user receives a score based on their correct answers.

## 🧰 Key Concepts Covered

- Data Structures (lists and dictionaries)
- Functions and Modular Code
- Loops (`for` loop)
- Conditional Statements (`if`, `elif`, `else`)
- User Input and Output
- Error Handling

## 🚀 How to Play the Quiz Game

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd quiz_game
Run the application:
bash
Copy code
python main.py
Follow the on-screen instructions to answer the quiz questions.
📖 Gameplay Instructions

The quiz consists of multiple-choice questions.
For each question, type the letter corresponding to your answer choice.
At the end of the quiz, your total score and percentage will be displayed.
Example Output:
less
Copy code
Welcome to the Simple Quiz Game!

Question 1:
What is the capital of France?
a) Berlin
b) London
c) Paris
d) Madrid
Your answer: c

Correct!

Question 2:
Which planet is known as the Red Planet?
a) Earth
b) Mars
c) Jupiter
d) Venus
Your answer: b

Correct!

You answered 2 out of 2 questions correctly.
Your score: 100%
🛠️ Code Overview

The application is structured with functions to manage different parts of the quiz:

run_quiz(questions): Runs through the list of questions and collects user answers.
check_answer(user_answer, correct_answer): Checks if the user's answer is correct.
Modules Used
No external modules are required.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this quiz game, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Data Structures

List of Dictionaries: Questions are stored as a list of dictionaries, each containing the question text, options, and correct answer. This structure allows for easy management and scalability.
2. Functions

run_quiz(questions): Handles the quiz flow, iterating over each question and collecting user input.
main(): Sets up the quiz data and calls run_quiz().
3. User Input Handling

Input Validation: Ensures the user enters a valid option (a, b, c, or d). Provides feedback if the input is invalid.
4. User Experience

Clear Prompts: Displays questions and options in a clear format.
Feedback Messages: Provides immediate feedback after each answer (Correct/Incorrect).
5. Scoring System

Score Calculation: Keeps track of the user's correct answers and calculates the percentage score at the end.
