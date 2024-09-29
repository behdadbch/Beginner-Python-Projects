import random

def get_random_word(word_list):
    """
    Selects a random word from the provided word list.
    """
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    """
    Displays the word with guessed letters revealed and underscores for remaining letters.
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_hangman(word):
    """
    Main game loop for Hangman.
    """
    attempts_remaining = 6
    guessed_letters = []
    word_letters = set(word)
    
    print("Welcome to Hangman!\n")

    while attempts_remaining > 0 and not word_letters.issubset(guessed_letters):
        print(f"Word to guess: {display_current_progress(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word_letters:
            print(f"Good guess!\n")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    if word_letters.issubset(guessed_letters):
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(f"Game Over! The word was '{word}'.")

def main():
    """
    Initializes the word list and starts the Hangman game.
    """
    word_list = ['python', 'hangman', 'challenge', 'programming', 'dataclass', 'function', 'variable', 'loop']
    word = get_random_word(word_list)
    play_hangman(word)

if __name__ == "__main__":
    main()