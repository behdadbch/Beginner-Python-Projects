

def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a divided by b.
    Handles division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def calculate(a, operator, b):
    """
    Calls the appropriate arithmetic function based on the operator.
    """
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    else:
        return "Invalid operator. Please use '+', '-', '*', or '/'."

def main():
    """
    Main function to run the calculator.
    """
    print("Welcome to the Basic Calculator!\n")

    while True:
        try:
            a = float(input("Enter the first number (or 'q' to quit): ").strip())
        except ValueError:
            print("Exiting the calculator. Goodbye!")
            break

        operator = input("Enter an operator (+, -, *, /): ").strip()

        try:
            b = float(input("Enter the second number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue

        result = calculate(a, operator, b)

        print(f"Result: {a} {operator} {b} = {result}\n")

if __name__ == "__main__":
    main()
