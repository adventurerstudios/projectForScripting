from datetime import datetime
import sqlite3
import hashlib
import re

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

#create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS UserData (
    USERNAME TEXT PRIMARY KEY UNIQUE,
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL UNIQUE
)
'''

)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_password(password):
    # At least 8 characters, one uppercase letter, and one number
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(pattern, password) is not None

def add_user(username, email, password):
    while True:
        if not is_valid_password(password):
            print("Password must be at least 8 characters long, contain a number, and an uppercase letter.")
            password = input("Enter a new valid password: ")
            continue

        try:
            hashed_password = hash_password(password)
            cursor.execute(
                "INSERT INTO UserData (username, password, email) VALUES (?, ?, ?)",
                (username, hashed_password, email)
            )
            conn.commit()
            return f"User '{username}' has been added"
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists. Please try again.")
            username = input("Enter a new username: ")
            email = input("Enter a new email: ")
            password = input("Enter a new password: ")


def authenticate_user(username, password_attempt):
   cursor.execute("SELECT password FROM UserData WHERE username = ?", (username,))
   result = cursor.fetchone()

   if result is None:
       return False, "User Not Found."

   stored_hash = result[0]
   hashed_attempt = hash_password(password_attempt)

   if stored_hash == hashed_attempt:
       return True, "Login Successful."

   return False, "Incorrect Password."


def get_user_info(username):
    authenticate_user(username, input("Enter password: "))
    cursor.execute("SELECT * FROM UserData WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        return None

    return {
        "username": user[0],
        "email": user[2]
}

def get_all_users(full_info=False):
    if full_info:
        cursor.execute("SELECT username, email, password FROM UserData")
    else:
        cursor.execute("SELECT username FROM UserData")
    result = cursor.fetchall()
    return result
def reset_database():
    cursor.execute('DELETE FROM UserData')
    conn.commit()
def add_user_direct(username, email, hashed_password):
    try:
        cursor.execute(
            "INSERT INTO UserData (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password))
        conn.commit()
        return f"User '{username}' has been imported successfully"
    except sqlite3.IntegrityError:
        return f"User '{username}' already exists"

import re

def check_for_leaks(scraped_data):
    cursor.execute("SELECT username, email FROM UserData")
    users = cursor.fetchall()
    leaks = []

    for user in users:
        username, email = user
        if re.search(re.escape(username), scraped_data) or re.search(re.escape(email), scraped_data):
            leaks.append((username, email))

    return leaks
