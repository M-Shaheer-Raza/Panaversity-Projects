import random

def generate_passwords(number, length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,"
    passwords = []

    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        passwords.append(password)

    return passwords


if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            number = int(input("Amount of passwords to generate: "))
            length = int(input("Enter your password length: "))
            
            if number <= 0 or length <= 0:
                print("Error: Please enter a positive number for both password count and length.")
            else:
                generated_passwords = generate_passwords(number, length)
                print("\nHere are your passwords:")
                for password in generated_passwords:
                    print(password)
                break
        
        except ValueError:
            print("Invalid input! Please enter valid integers for the number of passwords and password length.")