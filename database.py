import sqlite3
from pathlib import Path

# Define the path to the SQLite database file

base_dir = Path(__file__).resolve().parent
db_path = base_dir / 'login_database.db'

# Function to get a connection to the SQLite database

def get_connection():
    conn = sqlite3.connect(db_path)
    return conn

# Function to initialize the database and create the users table if it doesn't exist

def init_db():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
