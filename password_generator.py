import random
import string

def generate_password(length):
    # Combine all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for desired password length
try:
    user_length = int(input("Enter the desired password length: "))
    if user_length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        password = generate_password(user_length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
