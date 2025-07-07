import random
import string


def generate_password(length):
    # Define the possible characters: letters, digits, and punctuation
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # for password length
    if length < 4:
        print("Password should be at least 4 characters long.")
        return ""

    # Randomly picking characters one by one
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password


def main():
    print(" ----------Welcome to the Password Generator--------- ")

    # Asking the user how long they want their password
    try:
        user_input = input("Enter the password length: ")
        password_length = int(user_input)

        # Just double-checking if the input makes sense
        if password_length <= 0:
            print("Hmm... that doesn't look right. Please enter a positive number.")
            return

        # Call the function to generate the password
        new_password = generate_password(password_length)

        if new_password:
            print("Here's your strong password:",new_password)
            print("Make sure to keep it safe! 🙂")

    except ValueError:
        print("Please enter a positive integer.")


# Running the main function
if __name__ == "__main__":
    main()
