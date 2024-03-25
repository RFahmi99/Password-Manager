from cryptography.fernet import Fernet
from .database import connDatabase
import pyodbc


def getKey():
    try: 
        return connDatabase().execute("select key_value from Key where key_name = 'Key'").fetchone()[0].encode()
    except:
        return False


def setKey():
    key = Fernet.generate_key().decode()
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Code\Password-Manager\Data\Database.accdb;")
    cursor = conn.cursor()
    cursor.execute("UPDATE Key SET key_value = (?) WHERE key_name = 'Key'", (key))
    conn.commit()


def keyCheck():
    if getKey() == False:
        setKey()