import os
import string
import random
from cryptography.fernet import Fernet

# Define the character set (letters, numbers and special characters)
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

# Generate random substituion cipher
def gen_substitution_mapping():
    substitution_mapping = {}

    # Generate a unique random mapping for each character
    all_characters = list(CHARACTER_SET)
    for char in all_characters:
        mapping_length = random.randint(1, 4)
        # Randomly sample 'mapping_length' characters from the CHARACTER_SET
        substitution_mapping[char] = ''.join(random.sample(CHARACTER_SET, mapping_length))

    return substitution_mapping 


substitution_mapping = gen_substitution_mapping()

# Print the substitution mapping
print("Substitution Mapping:")
for original, substituted in substitution_mapping.items():
    print(f"{original}: {substituted}")