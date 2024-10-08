import sqlite3


def get_db():
    conn = sqlite3.connect("books.db")
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()

create_tables()