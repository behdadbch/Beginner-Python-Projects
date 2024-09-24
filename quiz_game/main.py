
def run_quiz(questions):
    """
    Runs the quiz by asking each question to the user.
    """
    score = 0
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}:")
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            if user_answer == question['answer']:
                print("\nCorrect!")
                score += 1
            else:
                print(f"\nIncorrect! The correct answer was '{question['answer']}'.")
        else:
            print("\nInvalid choice. Please enter a, b, c, or d.")
    return score

def main():
    """
    Main function to run the Simple Quiz Game.
    """
    print("Welcome to the Simple Quiz Game!")

    questions = [
        {
            'question': "What is the capital of France?",
            'options': ['a) Berlin', 'b) London', 'c) Paris', 'd) Madrid'],
            'answer': 'c'
        },
        {
            'question': "Which planet is known as the Red Planet?",
            'options': ['a) Earth', 'b) Mars', 'c) Jupiter', 'd) Venus'],
            'answer': 'b'
        },
        {
            'question': "Who wrote the play 'Romeo and Juliet'?",
            'options': ['a) William Shakespeare', 'b) Charles Dickens', 'c) Mark Twain', 'd) Jane Austen'],
            'answer': 'a'
        },
        {
            'question': "What is the largest mammal in the world?",
            'options': ['a) Elephant', 'b) Blue Whale', 'c) Great White Shark', 'd) Giraffe'],
            'answer': 'b'
        },
        {
            'question': "Which element has the chemical symbol 'O'?",
            'options': ['a) Gold', 'b) Oxygen', 'c) Silver', 'd) Iron'],
            'answer': 'b'
        }
    ]

    total_questions = len(questions)
    score = run_quiz(questions)
    percentage = (score / total_questions) * 100

    print(f"\nYou answered {score} out of {total_questions} questions correctly.")
    print(f"Your score: {percentage}%")

if __name__ == "__main__":
    main()
