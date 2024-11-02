import os

def save_substitution_mapping(substitution_mapping, account_name):
    """
    Save the substitution mapping to a file

    :param substitution_mapping: The substitution cipher that will be stored
    :return file_path: The path for the cipher mapping
    """
    # Get the directory of the current file (cipher folder)
    current_dir = os.path.dirname(__file__)

    # Navigate to the top level data folder
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    data_dir = os.path.join(project_root, "data", "ciphers")

    # Ensure the directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Generate file path with the format 'accountname_cipher.txt'
    file_name = f"{account_name}_cipher.txt"
    file_path = os.path.join(data_dir, file_name)

    # Save the mapping to a file in the chosen directory
    with open(file_path, 'w') as f:
        for original, substituted in substitution_mapping.items():
            f.write(f"{original}:{substituted}\n")

    return file_path

def delete_cipher_file(file_path):
    """
    Delete the cipher mapping file associated with the given account name.

    :param account_name: The name of the account whose cipher file will be deleted.
    :return: None
    """
    try:
        # Attempt to remove the file
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Cipher file {file_path} has been deleted.")
        else:
            print(f"Cipher file {file_path} does not exist.")
    except Exception as e:
        print(f"Error deleting cipher file: {e}")

def load_cipher_mapping(file_path):
    """
    Load the cipher mapping from a file where each line contains an original and substituted mapping.
    
    :param file_path: The path to the cipher mapping file.
    :return: Dictionary representing the cipher mapping.
    """
    cipher_mapping = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split only at the first occurrence of ':' to avoid unpacking issues
                parts = line.strip().split(':', 1)
                original, substituted = parts
                cipher_mapping[original] = substituted
    except FileNotFoundError:
        print(f"Cipher file {file_path} not found.")
    except Exception as e:
        print(f"Error loading cipher mapping: {e}")
    
    return cipher_mapping

def apply_cipher(text, cipher_mapping):
    """
    Apply the cipher mapping to the input text.
    
    :param text: The original text to be encrypted.
    :param cipher_mapping: Dictionary containing the cipher mapping.
    :return: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        # Get the mapped value or keep the character unchanged if not in the mapping
        encrypted_text += cipher_mapping.get(char, char)
    return encrypted_text

def gen_cipher_password(file_path, input_text):
    """
    Generate an encrypted password using the cipher mapping loaded from a file.
    
    :param file_path: The path to the cipher mapping file.
    :param text: The text to encrypt.
    :return: Encrypted text based on the cipher mapping.
    """
    cipher_mapping = load_cipher_mapping(file_path)
    encrypted_text = apply_cipher(input_text, cipher_mapping)
    return encrypted_text