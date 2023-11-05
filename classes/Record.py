import sqlite3
from .Token import Token

class Record:
    def __init__(self):
        self.connection = sqlite3.connect("example.db")
        self.cursor = self.connection.cursor()
    def verify(self, token):
        self.payload = Token().verify(token)
        return self
    def commit(self):
        self.cursor.execute(self.getStrModel())
        self.connection.commit()
        self.connection.close()
        return self 
    def data(self):
        self.cursor.execute(self.getStrModel())
        rows = self.cursor.fetchall()
        self.connection.close()
        return rows
    def roles(self, arr):
        if(self.payload["role"] in arr): 
            return self
        