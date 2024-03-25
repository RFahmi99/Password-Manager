from cryptography.fernet import Fernet
from .key import getKey


def encryption(password):
    key = getKey()
    fernet = Fernet(key)
    encPass = fernet.encrypt(password.encode())
    return encPass.decode()


def decryption(encPass):
    key = getKey()
    fernet = Fernet(key)
    decPass = fernet.decrypt(encPass).decode()
    return decPass