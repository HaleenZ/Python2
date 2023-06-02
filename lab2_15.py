import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 12
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
