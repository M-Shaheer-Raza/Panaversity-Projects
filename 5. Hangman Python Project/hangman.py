import random

def choose_word(word_list):
    return random.choice(word_list)

def display_current_state(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def get_user_guess(used_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha() and guess not in used_letters:
            return guess
        print("Invalid input or already guessed. Try again.")

def play_hangman():
    word_list = ['python', 'java', 'hangman', 'challenge', 'programming', 'developer']
    secret_word = choose_word(word_list)
    guessed_letters = set()
    wrong_guesses = set()
    allowed_mistakes = 6

    print("\nWelcome to Hangman!")
    print("Try to guess the secret word, one letter at a time.")
    print(f"You are allowed {allowed_mistakes} incorrect guesses.")

    while True:
        print("\nWord: " + display_current_state(secret_word, guessed_letters))
        print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
        print("Remaining mistakes:", allowed_mistakes - len(wrong_guesses))

        guess = get_user_guess(guessed_letters.union(wrong_guesses))

        if guess in secret_word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            wrong_guesses.add(guess)
            print("Sorry, that letter is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        if len(wrong_guesses) >= allowed_mistakes:
            print("\nGame Over! You've run out of guesses.")
            print("The secret word was:", secret_word)
            break

def main():
    while True:
        play_hangman()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thanks for playing Hangman! Goodbye.")
            break

if __name__ == "__main__":
    main()