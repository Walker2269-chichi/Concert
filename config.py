# config.py
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('DB/concerts.db')
cursor = conn.cursor()

def get_cursor():
    """Returns the database cursor."""
    return cursor

def commit():
    """Commits changes to the database."""
    conn.commit()

def close():
    """Closes the database connection."""
    conn.close()

def initialize_db():
    """Initializes the database by running the SQL scripts."""
    with open('scripts/tables.sql', 'r') as f:
        cursor.executescript(f.read())
