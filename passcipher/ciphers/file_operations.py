import os
from passcipher.encrypt import encrypt_data, decrypt_data

def save_substitution_mapping(substitution_mapping, account_name, key):
    """
    Save the substitution mapping to a file after encrypting it.

    :param substitution_mapping: The substitution cipher that will be stored
    :param account_name: The name of the account for which the cipher mapping is saved
    :param key: The encryption key used to encrypt the mapping
    :return: file_path: The path for the cipher mapping
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

    # Convert mapping to string format
    mapping_string = "\n".join(f"{original}:{substituted}" for original, substituted in substitution_mapping.items())

    # Encrypt the mapping string
    encrypted_mapping = encrypt_data(key, mapping_string)

    # Save the encrypted mapping to a file
    with open(file_path, 'w') as f:
        f.write(encrypted_mapping)

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

def load_cipher_mapping(key, file_path):
    """
    Load the cipher mapping from a file and decrypt it.
    
    :param file_path: The path to the cipher mapping file.
    :param key: The encryption key used to decrypt the mapping
    :return: Dictionary representing the cipher mapping.
    """
    cipher_mapping = {}
    try:
        with open(file_path, 'r') as file:
            encrypted_mapping = file.read()
            # Decrypt the mapping string
            mapping_string = decrypt_data(key, encrypted_mapping)

            # Split into lines and create the mapping
            for line in mapping_string.splitlines():
                parts = line.strip().split(':', 1)
                if len(parts) == 2:
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

def gen_cipher_password(key, file_path, input_text):
    """
    Generate an encrypted password using the cipher mapping loaded from a file.
    
    :param file_path: The path to the cipher mapping file.
    :param text: The text to encrypt.
    :return: Encrypted text based on the cipher mapping.
    """
    cipher_mapping = load_cipher_mapping(key, file_path)
    encrypted_text = apply_cipher(input_text, cipher_mapping)
    return encrypted_text