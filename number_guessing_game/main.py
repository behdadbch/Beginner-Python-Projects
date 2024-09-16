
import random

def play_number_guessing_game():
    """
    Starts the Number Guessing Game where the player tries to guess a randomly selected number.
    """
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            guess = input("Enter your guess: ")
            guess = int(guess)
            number_of_guesses += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.\n")
            elif guess > number_to_guess:
                print("Too high! Try again.\n")
            else:
                print(f"Congratulations! You guessed the number in {number_of_guesses} tries!\n")
                break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.\n")

def main():
    """
    Manages the game sessions and replay functionality.
    """
    while True:
        play_number_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print("Thank you for playing!")
            break
        print()  # Add a blank line for better readability between games

if __name__ == "__main__":
    main()
