# Password Generator

## 🔑 Description

The **Password Generator** is a command-line application that generates random passwords based on user-defined criteria. Users can specify the length of the password and choose whether to include uppercase letters, lowercase letters, numbers, and special characters.

## 🧰 Key Concepts Covered

- String Manipulation
- Random Number Generation (`random` module)
- User Input and Output
- Conditional Statements (`if`, `elif`, `else`)
- Functions and Modular Code

## 🚀 How to Use the Password Generator

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd password_generator
Run the application:
bash
Copy code
python main.py
Follow the on-screen instructions to generate a password.
📖 Usage Instructions

Upon running the application, you will be prompted to:

Enter the desired password length.
Choose whether to include uppercase letters.
Choose whether to include lowercase letters.
Choose whether to include numbers.
Choose whether to include special characters.
The application will then generate a random password based on the criteria selected.

Example Output:
bash
Copy code
Welcome to the Password Generator!

Enter the desired password length (8-20): 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: A3f9kH1lq2Tz
🛠️ Code Overview

The application is structured with functions for each task:

generate_password(length, use_upper, use_lower, use_numbers, use_special): Generates a random password based on user preferences.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this password generator, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Modular Functions

generate_password(): Encapsulates the logic for generating a random password. This modular design allows for easier testing and modifications.
2. String Manipulation

Character Sets: Uses the string module to access predefined character sets (uppercase, lowercase, digits, punctuation) for easy manipulation.
3. User Input Handling

Length Validation: Ensures the user enters a valid password length (between 8 and 20). Uses a try-except block to handle invalid inputs.
Boolean Flags: Captures user preferences for different character types using boolean values.
4. Randomness

Random Character Selection: Uses a list comprehension and random.choice() to generate the password based on user-defined criteria.
5. User Experience

Clear Prompts: Guides the user through each step of the password generation process.
Feedback Messages: Displays the generated password and prompts the user to generate another one or exit.
6. Error Handling

Character Type Selection: Checks if at least one character type is selected and returns an appropriate error message if not.
