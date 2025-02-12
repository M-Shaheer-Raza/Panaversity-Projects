import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    
    return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        play_round()
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()