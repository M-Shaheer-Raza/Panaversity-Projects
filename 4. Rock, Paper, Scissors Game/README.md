# Rock, Paper, Scissors Game  

## Overview  
The **Rock, Paper, Scissors Game** is a simple command-line game where a user plays against the computer. The player chooses either **rock**, **paper**, or **scissors**, and the computer randomly selects one as well. The winner is determined based on the standard game rules.  

## Features  
- Interactive gameplay with user input  
- Randomized computer choices for fair play  
- Simple text-based interface for easy play  
- Ability to play multiple rounds  

## How to Play?  
1. The game will ask you to enter **rock**, **paper**, or **scissors**.  
2. The computer will randomly pick one of the three options.  
3. The game will announce the winner based on the following rules:  
   - **Rock beats Scissors**  
   - **Paper beats Rock**  
   - **Scissors beats Paper**  
   - If both choices are the same, it’s a **tie**  
4. After each round, you can choose to **play again** or **exit**.  

## Project Structure  
```
Project_4_Rock_Paper_Scissors/
│── rock_paper_scissors.py  # Main script
│── README.md               # Project documentation
```

## Code Explanation  
- `get_user_choice()`: Prompts the user for input and validates their choice.  
- `get_computer_choice()`: Randomly selects rock, paper, or scissors for the computer.  
- `determine_winner()`: Compares user and computer choices and decides the winner.  
- `play_round()`: Runs a single round of the game.  
- `main()`: Handles multiple rounds and allows the user to replay.  

## Example Output  
```
Welcome to Rock, Paper, Scissors!
Enter your choice (rock, paper, or scissors): rock

You chose: rock
Computer chose: scissors
Congratulations! You win!

Do you want to play again? (yes/no): yes
```