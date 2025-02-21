import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Timer Completed!")

if __name__ == "__main__":
    while True:
        try:
            t = int(input("Enter the time in seconds: "))
            if t <= 0:
                print("Please enter a positive number for the countdown time.")
            else:
                countdown(t)
                break
        except ValueError:
            print("Invalid input! Please enter a valid number of seconds.")