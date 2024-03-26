import pyodbc


def connDatabase():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Path\To\Your\Code\Password-Manager\Data\Database.accdb;")
    return conn.cursor()
