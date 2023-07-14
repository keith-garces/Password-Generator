import random
import string

def generate_password(length=20):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
password = generate_password()
print(password)
    