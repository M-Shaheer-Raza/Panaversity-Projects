## **Guess the Number Game (Computer)**  

### **Overview**  
The **Guess the Number Game** is a fun interactive Python game where the computer randomly selects a number within a given range, and the player must guess it. The game provides feedback on each guess, indicating whether it is too high or too low, until the player correctly identifies the number.  

### **Features**  
- Random number generation using Python’s `random` module  
- User-friendly input validation  
- Unlimited attempts until the correct number is guessed  
- Feedback system guiding the player to the correct answer  

### **How to Play?**  
1. Run the script in a Python environment.  
2. The computer randomly selects a number between **1 and 10**.  
3. The player enters a guess, and the program provides hints:  
   - **Too low!** → Guess a higher number  
   - **Too high!** → Guess a lower number  
   - **Correct!** → The game ends, showing the number of attempts  
4. The player continues guessing until they find the correct number.  

### **Project Structure**  
```
Project_2_Guess_Number_Computer/
│── guess_the_number.py  # Main script
│── README.md            # Project documentation
```

### **Code Explanation**  
- The `random.randint(1, x)` function selects a random number within a given range.  
- The `while True` loop allows the user to keep guessing until they get the correct answer.  
- The `try-except` block ensures that the user inputs a valid integer.  
- If the guessed number is incorrect, hints are given to help the player adjust their guess.  

### **Example Output**  
```
Welcome to the Guess the Number Game!
I have selected a number between 1 and 10. Try to guess it!
Enter your guess: 5
Too high! Try again.
Enter your guess: 2
Too low! Try again.
Enter your guess: 3
Congratulations! You guessed the number in 3 attempts.
```