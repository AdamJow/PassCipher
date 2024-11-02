from cryptography.fernet import Fernet

def generate_key(username):
    """
    Generates a unique encryption key for the user and saves it to a file
    """
    key = Fernet.generate_key()
    with open(f"{username}_key.txt", "w") as f:
        f.write(key.decode("utf-8"))
    return key

def encrypt_data(key, data):
    """
    Encrypts data using key.
    
    :param key: The key used to encypt data
    :param data: The data to be encrypted
    :return: The encypted encrypted data
    """
    fernet = Fernet(key)
    # Encodes to bytes for encryption and then decodes to a string for easier storage or display
    encrypted_data = fernet.encrypt(data.encode("utf-8")).decode("utf-8")
    return encrypted_data

def decrypt_data(key, data):
    """
    Encrypts data using key.
    
    :param key: The key used to encypt data
    :param data: The data to be encrypted
    :return: The encypted encrypted data
    """
    fernet = Fernet(key)
    # Encodes to bytes for encryption and then decodes to a string for easier storage or display
    encrypted_data = fernet.decrypt(data.encode("utf-8")).decode("utf-8")
    return encrypted_data

def verify_login_key(login_key, verify_text):
    """
    Attempts to decrypt the verify text using the login key.
    
    :param login_key: The inputted login key by user
    :param verify_text: The stored verify text in the user database
    :return: True if the verify text can be decrypted, false if it cannot
    """
    try:
        f = Fernet(login_key)
        f.decrypt(verify_text.encode('utf-8'))
        return True
    except:
        return False