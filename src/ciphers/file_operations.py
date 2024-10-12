import os

# Save the substitution mapping to a file
def save_substitution_mapping(substitution_mapping):
    # Default to user's Documents folder
    default_dir = os.path.join(os.path.expanduser("~"), "Documents", "PassCipherFiles")
    
    # Ask user if they want to specify a different directory
    print(f"Default save directory: {default_dir}")
    storage_dir = input("Enter a custom directory (or press Enter to use the default): ")
    
    # If no directory is provided, use the default directory
    if not storage_dir:
        storage_dir = default_dir

    # Ensure the directory exists
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)

    # Save the mapping to a file in the chosen directory
    file_path = os.path.join(storage_dir, "cipher.txt")
    with open(file_path, 'w') as f:
        for original, substituted in substitution_mapping.items():
            f.write(f"{original}:{substituted}\n")
    
    print(f"Substitution cipher saved to {file_path}")