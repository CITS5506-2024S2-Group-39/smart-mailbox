import hashlib

# Optional: Hash the password
def hash_password(password):
    return password

# Store the hashed password in a file (backend)
def store_password(password):
    hashed_password = hash_password(password)
    with open('password.txt', 'w') as file:
        file.write(hashed_password)

# Load the hashed password from the file
def load_password():
    try:
        with open('password.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        # Default Password
        return '000000'

# Verify the input password by comparing its hash to the stored hash
def verify_password(input_password):
    stored_password = load_password()
    return stored_password == hash_password(input_password)
