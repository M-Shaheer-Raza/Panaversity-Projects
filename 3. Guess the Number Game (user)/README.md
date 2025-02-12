## **Guess the Number Game (User)**  

### **Overview**  
The **Guess the Number Game (User)** is an interactive Python game where the **computer tries to guess the number** that the user is thinking of. The user provides feedback on whether the computer's guess is too high, too low, or correct, and the computer adjusts its guesses accordingly.  

### **Features**  
- The computer attempts to guess the user's secret number.  
- Uses **binary search logic** to minimize the number of guesses.  
- Interactive gameplay with user feedback.  
- Beginner-friendly Python project.  

### **How to Play?**  
1. Think of a secret number between **1 and X** (default is 10).  
2. The computer will make a guess.  
3. Provide feedback:  
   - Type **H** if the guess is **too high**  
   - Type **L** if the guess is **too low**  
   - Type **C** if the guess is **correct**  
4. The game continues until the computer correctly guesses your number.  

### **Project Structure**  
```
Project_3_Guess_Number_User/
│── guess_number_user.py  # Main script
│── README.md             # Project documentation
```

### **Code Explanation**  
- The computer randomly picks a number within the given range.  
- The user provides feedback (high, low, or correct).  
- The computer narrows down the guessing range using **binary search logic**.  
- The process repeats until the computer guesses the correct number.  

### **Example Output**  
```
Think of a secret number between 1 and 10, and I'll try to guess it using random guesses!
My guess is: 7
Is my guess too high (H), too low (L), or correct (C)? L
My guess is: 9
Is my guess too high (H), too low (L), or correct (C)? H
My guess is: 8
Is my guess too high (H), too low (L), or correct (C)? C
Yay! I guessed your number in 3 attempts!
```