import time
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_time():
    while True:
        try:
            user_input = input("Enter the countdown time in seconds: ").strip()
            seconds = int(user_input)
            if seconds > 0:
                return seconds
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def countdown_timer(seconds):
    try:
        for remaining in range(seconds, 0, -1):
            clear_console()
            print("Countdown Timer")
            print(f"Time remaining: {remaining} second{'s' if remaining != 1 else ''}")
            time.sleep(1)
        clear_console()
        print("Time's up!")
    except KeyboardInterrupt:
        print("\nCountdown cancelled.")
        sys.exit()

def main():
    seconds = get_user_time()
    countdown_timer(seconds)

if __name__ == "__main__":
    main()