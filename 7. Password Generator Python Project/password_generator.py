import random
import string

def get_password_options():
    while True:
        try:
            length = int(input("Enter the desired password length (positive integer): "))
            if length > 0:
                break
            print("Password length must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() in ['yes', 'y']
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() in ['yes', 'y']
    include_digits = input("Include digits? (yes/no): ").strip().lower() in ['yes', 'y']
    include_symbols = input("Include special symbols? (yes/no): ").strip().lower() in ['yes', 'y']

    if not (include_uppercase or include_lowercase or include_digits or include_symbols):
        print("You must select at least one character type. Let's try again.\n")
        return get_password_options()

    return length, include_uppercase, include_lowercase, include_digits, include_symbols

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_lowercase, include_digits, include_symbols = get_password_options()
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()