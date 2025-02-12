# Mad Libs Python Project  

## Overview  
The **Mad Libs Python Project** is an interactive word-based game where users provide different types of words (adjectives, nouns, verbs, etc.), which are then placed into a predefined story. This results in a unique and often funny story every time the program runs.  

## Features  
- Interactive user input  
- Generates a unique and fun story each time  
- Uses **f-string formatting** for dynamic story generation  
- Beginner-friendly and great for practicing Python basics  

## How to Play?  
1. Run the script in a Python environment.  
2. The program will ask for different types of words (e.g., adjectives, nouns, verbs).  
3. After all inputs are provided, a custom-generated story will be displayed based on the user's words.  

## Project Structure  
```
Project_1_Mad_Libs/
│── mad_libs.py  # Main script
│── README.md    # Project documentation
```

## Code Explanation  
- The `get_input()` function prompts the user to enter words and returns the input.  
- The `create_story()` function collects user input and inserts it into a predefined template using **f-strings**.  
- The final story is printed out dynamically based on user input.  

## Example Output  
```
Welcome to the Mad Libs Game!
Enter an adjective: magical
Enter a noun: wizard
Enter a verb: dance
Enter an adverb: happily
Enter a plural noun: stars

Here's your story:
Once upon a time, there was a magical wizard who loved to dance happily.  
Every day, the wizard would join a group of stars to celebrate the joys of life.
```