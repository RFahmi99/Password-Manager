import pyodbc


def connDatabase():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Code\Password-Manager\Data\Database.accdb;")
    return conn.cursor()