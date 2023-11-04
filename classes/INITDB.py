import sqlite3

class INITDB:
    def __init__(self):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE users (password, name, telephone, email, role);")
        con.close()