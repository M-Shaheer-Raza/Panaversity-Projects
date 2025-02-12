import random

def guess_the_number(x):
    secret_number = random.randint(1, x)
    guess_count = 0

    print("Welcome to the Guess the Number Game!")
    print(f"I have selected a number between 1 and {x}. Try to guess it!")

    while True:
        user_input = input("Enter your guess: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        guess_count += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guess_count} attempts.")
            break

if __name__ == "__main__":
    guess_the_number(10)