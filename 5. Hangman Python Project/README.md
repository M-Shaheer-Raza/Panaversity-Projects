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
Hangman_Python_Project/
│── hangman.py   # Main script
│── words.py     # Word list for the game
│── hangman_visual.py # Visual representation of the hangman figure
│── README.md    # Project documentation
```

### **Code Explanation**  
- **`get_valid_word(words)`** → Selects a random word from the list of words.  
- **`hangman()`** → Main game function that runs one round of Hangman.  
- **`lives_visual_dict`** → A dictionary containing visual representations of the hangman for each stage of the game.  
- **`input()`** → Used to prompt the player to guess a letter.  
- **`while` loop** → Controls the game flow and keeps track of the player's guesses and lives.

### **Example Output**  
```
You have 7 lives left and you have used these letters:  
Current word:  _ _ _ _ _ _
You have 6 lives left and you have used these letters: A
Current word:  A _ _ _ _ _
Guess a letter: B
Your letter, B is not in the word.
You have 5 lives left and you have used these letters: A B
Current word:  A _ _ _ _ _
...
YAY! You guessed the word!
```