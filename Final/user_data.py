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
    try:
        cursor.execute("INSERT INTO UserData (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        return f"User '{username}' has been added"
    except sqlite3.IntegrityError:
        return f"User '{username}' already exists"

def authenticate_user(username, password_attempt):
   cursor.execute("SELECT password FROM UserData WHERE username = ?", (username,))
   result = cursor.fetchone()

   if result is None:
       return False, "User Not Found."


def get_user_info(username):
    authenticate_user(username, input("Enter password: "))
    cursor.execute("SELECT * FROM UserData WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        return None

    return {
        "username": user[0],
        "email": user[1]
}

def get_all_users():
    cursor.execute("SELECT USERNAME FROM UserData")
    result = cursor.fetchall()
    return result
def reset_database():
    cursor.execute('DELETE FROM UserData')
    conn.commit()