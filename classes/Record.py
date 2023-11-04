import sqlite3

class Record:
    def __init__(self):
        self.connection = sqlite3.connect("example.db")
        self.cursor = self.connection.cursor()
    def verify(self, token):
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