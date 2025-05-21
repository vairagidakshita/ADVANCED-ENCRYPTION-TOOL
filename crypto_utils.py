from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[✔] Key generated and saved as 'secret.key'")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"[✔] Encrypted file saved as: {filename}.enc")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    output_file = filename.replace(".enc", "")
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"[✔] Decrypted file saved as: {output_file}")
