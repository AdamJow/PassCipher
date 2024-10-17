import string
import secrets # More secure than random library

# Define the character set (letters, numbers and special characters)
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

# Generate random substituion cipher
def gen_substitution_mapping():
    substitution_mapping = {}

    # Generate a unique random mapping for each character
    for char in CHARACTER_SET:
        # Random number between 1 and 4 inclusive (all characters will have a mapping)
        mapping_length = secrets.randbelow(4) + 1
        # Randomly sample 'mapping_length' characters from the CHARACTER_SET
        substitution_mapping[char] = ''.join(secrets.choice(CHARACTER_SET) for i in range(mapping_length))

    return substitution_mapping 