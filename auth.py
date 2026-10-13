import sqlite3
import bcrypt
from database import get_connection

# Function to register a new user in the database and hash their password using bcrypt

def register_user(username, password):
    error = validate_credentials(username, password)
    if error:
        return False, error

    username = username.strip()

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        return True, "User registered successfully."
    except sqlite3.IntegrityError:
        return False, "Username already exists."
    finally:
        conn.close()

# Function to validate user credentials before registration

def validate_credentials(username, password):
    username = username.strip()

    if not username or not password:
        return "Fill in all fields. "
    if len(username) < 3:
        return "The username needs to have at least 3 characters."
    if len(password) < 6:
        return "The password needs to have at least 6 characters."
    return None

# Function to log in a user by checking their credentials against the database

def login(username, password):
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT password FROM users WHERE username = ?",
            (username,)
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        return False, "Invalid username or password."

    stored_hash = row[0].encode()
    return bcrypt.checkpw(password.encode(), stored_hash)