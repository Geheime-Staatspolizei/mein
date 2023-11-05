import sqlite3
from classes.Roles import ADMIN_ROLE
from classes.Roles import USER_ROLE
from classes.Roles import ROOT_ROLE

class FIRSTEVERROOT:
    def __init__(self, email):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role = {ROOT_ROLE} WHERE email = '{email}';")
        con.commit()
        con.close()