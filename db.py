import sqlite3
from flask import g

class Db_oject:
    def __init__(self):
        pass

    @staticmethod
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect("instance/users.db")
        return db

    @property
    def con(self):
        return self.get_db()
    
    @property
    def cur(self):
        return self.con.cursor()