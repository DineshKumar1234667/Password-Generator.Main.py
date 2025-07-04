import random
import string

def generate_password(length):
    """
    Generates a random password of a specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be a positive integer.")
        else:
            new_password = generate_password(password_length)
            print(f"Generated Password: {new_password}")
    except ValueError:
        print("Invalid input. Please enter an integer for the password length.")
