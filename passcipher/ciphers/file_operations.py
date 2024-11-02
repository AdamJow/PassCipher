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