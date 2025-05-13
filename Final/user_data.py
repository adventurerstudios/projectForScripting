from datetime import datetime

user_database = {}

def add_user(username, email, password):
    if username in user_database:
        return f"User '{username}' already exists."
    user_database[username] = {
        "email": email,
        "password": password,
        "login_history": [],
        "password_attempts": []
    }
    return f"User '{username}' added successfully."

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