import random
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
def display_instructions():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules:")
    print("1.Rock beats Scissors")
    print("2.Scissors beats Paper")
    print("3.Paper beats Rock")
    print("Enter 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")
    print()

def get_user_choice():
    while True:
        user_input = input("Your choice: ").lower()
        if user_input in choices:
            return user_input
        elif user_input == 'exit':
            return None
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score

    user_choice = get_user_choice()
    if user_choice is None:
        return False  # Exit game

    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win this round!")
        user_score += 1
    else:
        print("Result: Computer wins this round!")
        computer_score += 1

    print(f"Score => You: {user_score} | Computer: {computer_score}")
    print("-" * 30)
    return True

# Main game loop
def main():
    display_instructions()

    while True:
        continue_game = play_round()
        if not continue_game:
            break

    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
