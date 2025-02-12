import random

def computer_guess_game(x):

    print(f"Think of a secret number between 1 and {x}, and I'll try to guess it using random guesses!")

    low = 1
    high = x
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == "C":
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        elif feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        else:
            print("Invalid input. Please respond with H, L, or C.")

    else:
        print("Your responses seem inconsistent. Please try again.")

if __name__ == "__main__":
    computer_guess_game(10)