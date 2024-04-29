import sqlite3


def connection():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        content BLOB NOT NULL,
        iv BLOB NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )""")
    return conn, c

def list():
    conn, c = connection()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return notes

def get(id: int):
    conn, c = connection()
    c.execute("SELECT * FROM notes WHERE id = ?", (id,))
    note = c.fetchone()
    conn.close()
    return note

def insert(content: str, iv: str):
    conn, c = connection()
    c.execute("INSERT INTO notes (content, iv, created_at, updated_at) VALUES (?, ?, datetime('now'), datetime('now'))", (content, iv))
    conn.commit()
    conn.close()
    return c.lastrowid

def update(id: int, content: str, iv: str):
    conn, c = connection()
    c.execute("UPDATE notes SET content = ?, iv = ?, updated_at = datetime('now') WHERE id = ?", (content, iv, id))
    conn.commit()
    conn.close()

def delete(id):
    conn, c = connection()
    c.execute("DELETE FROM notes WHERE id = ?", (id,))
    conn.commit()
    conn.close()