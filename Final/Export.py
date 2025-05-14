from Final.user_data import get_all_users

def export ():
    while True:
        choose = input("Would you like to export all users to a new file? (y/n): ")
        if choose.lower() == "y":
            filename = input("What would you like to name the file?: ")
            with open(filename, "w", encoding="utf-8") as file:
                print(f"File {filename} has been created!")

                file.write(str(get_all_users(full_info=True)))
                break
        elif choose == "n":
            break
        else:
            print("Invalid input. Please try again.")
            return

from Final.user_data import add_user_direct

def import_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            users = eval(file.read())
            for user in users:
                username, email, hashed_password = user
                print(add_user_direct(username, email, hashed_password))
        print("Import complete.")
    except Exception as e:
        print(f"Import failed: {e}")
