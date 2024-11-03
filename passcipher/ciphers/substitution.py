import secrets # More secure than random library

def gen_substitution_mapping(character_set):
    """
    Generate random substituion cipher

    :return: The substituion mapping
    """
    substitution_mapping = {}

    # Generate a unique random mapping for each character
    for char in character_set:
        # Random number between 1 and 4 inclusive (all characters will have a mapping)
        mapping_length = secrets.randbelow(4) + 1
        # Randomly sample 'mapping_length' characters from the CHARACTER_SET
        substitution_mapping[char] = ''.join(secrets.choice(character_set) for i in range(mapping_length))

    return substitution_mapping 