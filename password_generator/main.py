
import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    """
    Generates a random password based on the specified criteria.
    """
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to run the Password Generator.
    """
    print("Welcome to the Password Generator!\n")

    while True:
        try:
            length = int(input("Enter the desired password length (8-20): "))
            if length < 8 or length > 20:
                raise ValueError("Length must be between 8 and 20.")
        except ValueError as e:
            print(e)
            continue

        use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lower = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
        
        if "Error" in password:
            print(password)
        else:
            print(f"\nGenerated Password: {password}\n")

        play_again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for using the Password Generator! Goodbye!")
            break

if __name__ == "__main__":
    main()
