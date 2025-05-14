from datetime import datetime
import sqlite3
import hashlib

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

#create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS UserData (
    USERNAME TEXT PRIMARY KEY,
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL
)
'''

)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, email, password):
    try:
        hashed_password = hash_password(password)
        cursor.execute(
            "INSERT INTO UserData (username, password, email) VALUES (?, ?, ?)",
            (username, email, hashed_password))
        conn.commit()
        return f"User '{username}' has been added"
    except sqlite3.IntegrityError:
        return f"User '{username}' already exists"

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

def get_all_users():
    cursor.execute("SELECT USERNAME FROM UserData")
    result = cursor.fetchall()
    return result
def reset_database():
    cursor.execute('DELETE FROM UserData')
    conn.commit()

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
