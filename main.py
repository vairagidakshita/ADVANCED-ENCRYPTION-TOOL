import os
from crypto_utils import generate_key, encrypt_file, decrypt_file

def menu():
    print("\n=== AES-256 File Encryption Tool ===")
    print("1. Generate New Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    print("4. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter the file name (e.g., notes.txt): ")
        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print("File not found!")

    elif choice == "3":
        filename = input("Enter the encrypted file name (e.g., notes.txt.enc): ")
        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print("File not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
