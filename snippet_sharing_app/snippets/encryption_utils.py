from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt the data using the provided key
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Decrypt the data using the provided key
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt the data using the provided key
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Decrypt the data using the provided key
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()
