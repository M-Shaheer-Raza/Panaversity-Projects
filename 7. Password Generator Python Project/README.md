# Password Generator Python Project

## Description
This Python program generates random, secure passwords based on user input. Users can specify the number of passwords to generate and the desired length for each password. The program ensures that the passwords contain a mix of letters, digits, and special characters.

## Features
- User-defined number of passwords to generate.
- Option to set the password length.
- Generates secure, random passwords with a variety of characters (uppercase, lowercase, digits, and symbols).
- Input validation to ensure positive integer values for both the number of passwords and the password length.

## How It Works
1. The program asks the user for the number of passwords to generate and the desired length.
2. It validates that both inputs are positive integers.
3. It generates the specified number of passwords, each with the specified length.
4. The generated passwords are displayed to the user.

## Project Structure
```
Password-Generator/
│── password_generator.py  # Main script
│── README.md             # Project documentation
```

## Example Output
```
Welcome to the Password Generator!
Amount of passwords to generate: 3
Enter your password length: 8

Here are your passwords:
aG9r#8yA
zZ!1kLwP
E5a@NxQ8
```