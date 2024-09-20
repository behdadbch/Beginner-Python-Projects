import random

def get_computer_choice():
    """
    Randomly selects Rock, Paper, or Scissors for the computer.
    """
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """
    Determines the winner based on player and computer choices.
    """
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        print("Choose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            player_input = int(input("Enter your choice (1-3): "))
            if player_input < 1 or player_input > 3:
                raise ValueError

            player_choice = ['Rock', 'Paper', 'Scissors'][player_input - 1]
            computer_choice = get_computer_choice()

            print(f"\nYou chose {player_choice}. The computer chose {computer_choice}.")
            print(determine_winner(player_choice, computer_choice))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")
            continue

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()