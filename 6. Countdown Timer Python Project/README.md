# Countdown Timer Python Project

## Description
The Countdown Timer is a Python program that allows users to input a countdown duration in seconds. It then counts down from the specified time, displaying the remaining time in `MM:SS` format. Once the time reaches zero, a message is shown indicating that the timer has completed.

## Features
- Accepts user input for the countdown time in seconds.
- Displays the countdown in `MM:SS` format.
- Validates input to ensure the entered value is a positive integer.
- Repeats the prompt until a valid input is provided.
- Displays "Timer Completed!" when the countdown finishes.

## How It Works
1. The program asks the user for the desired countdown time in seconds.
2. The user is prompted until a valid positive integer is provided.
3. The countdown starts and the remaining time is displayed in `MM:SS` format.
4. The program waits for 1 second between each countdown update.
5. Once the timer reaches zero, the program prints "Timer Completed!" to indicate the end.

## Project Structure
```
Countdown-Timer/
│── countdown_timer.py  # Main script
│── README.md           # Project documentation
```

## Example Output
```
Enter the time in seconds: 120
02:00
01:59
...
Timer Completed!
```