from .cryptography import *
from .database import connDatabase
import pyodbc


def writePass(passName, passWord):
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Path\To\Your\Code\Password-Manager\Data\Database.accdb;")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Data (data_name, data_pass) VALUES (?, ?)", (passName, encryption(passWord)))
    conn.commit()
    pass


def showPass(passName):
    try:
        return decryption(connDatabase().execute("SELECT data_pass FROM Data WHERE data_name = (?)", (passName)).fetchone()[0])
    except:
        return "There is no password saved with this name. Please try again."
