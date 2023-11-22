import sqlite3
from sqlite3 import Error

def create_connection(path: str):
    try:
        return sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")
