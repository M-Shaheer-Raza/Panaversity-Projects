# **Hangman Python Project**  

### **Overview**  
The **Hangman Python Project** is a word-guessing game where the player tries to guess a secret word by guessing one letter at a time. The player has a limited number of incorrect guesses before the game is over.  

### **Features**  
- Random word selection from a predefined list  
- Displays the current progress with underscores for unguessed letters  
- Tracks wrong guesses and limits the number of mistakes  
- Interactive and user-friendly gameplay  
- Great for practicing **Python loops, conditionals, and sets**  

### **How to Play?**  
1. The program selects a random word from a predefined list.  
2. The player guesses one letter at a time.  
3. Correct guesses reveal the letter in the word.  
4. Incorrect guesses are tracked, and the player has a limited number of mistakes.  
5. The game ends when the player correctly guesses the word or runs out of attempts.  

### **Project Structure**  
```
Project_5_Hangman/
│── hangman.py   # Main script
│── README.md    # Project documentation
```

### **Code Explanation**  
- **`choose_word(word_list)`** → Selects a random word from the list.  
- **`display_current_state(secret_word, guessed_letters)`** → Displays the word with guessed letters and underscores.  
- **`get_user_guess(used_letters)`** → Gets and validates user input.  
- **`play_hangman()`** → Main game function that runs one round of Hangman.  
- **`main()`** → Allows the user to play multiple rounds.  

### **Example Output**  
```
Welcome to Hangman!
Try to guess the secret word, one letter at a time.
You are allowed 6 incorrect guesses.

Word: _ _ _ _ _ _
Guess a letter: p
Good guess!

Word: p _ _ _ _ _
Guess a letter: z
Sorry, that letter is not in the word.
Wrong guesses: z
Remaining mistakes: 5

...
Congratulations! You guessed the word: python
```