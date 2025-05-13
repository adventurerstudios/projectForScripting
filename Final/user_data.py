from datetime import datetime
import sqlite3

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

def add_user(username, email, password):

def authenticate_user(username, password_attempt):
    if username not in user_database:
        return False, "User not found."

    user = user_database[username]
    user["password_attempts"].append((password_attempt, datetime.now().isoformat()))

    if user["password"] == password_attempt:
        user["login_history"].append(datetime.now().isoformat())
        return True, "Login successful."
    else:
        return False, "Incorrect password."

def get_user_info(username):
    return user_database.get(username, None)

def get_all_users():
    return list(user_database.keys())

def reset_database():
    global user_database
    user_database = {}