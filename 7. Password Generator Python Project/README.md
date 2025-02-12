# Password Generator Python Project

## Description
The Password Generator is a Python program that creates strong, randomized passwords based on user preferences. Users can specify the password length and choose to include uppercase letters, lowercase letters, digits, and special symbols.

## Features
- User-defined password length
- Option to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special symbols
- Ensures at least one character type is selected
- Generates a secure password randomly

## How It Works
1. The program asks the user for the desired password length.
2. The user chooses which types of characters to include.
3. The program generates a password with random characters from the selected categories.
4. The password is displayed on the screen.

## Project Structure
```
Password-Generator/
│── password_generator.py  # Main script
│── README.md              # Project documentation
```

## Example Output
```
Welcome to the Password Generator!
Enter the desired password length (positive integer): 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include digits? (yes/no): yes
Include special symbols? (yes/no): no

Generated Password:
G8rTpM2yXqkL
```