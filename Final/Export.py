from Final.user_data import get_all_users


def export ():
    while True:
        choose = input("Would you like to export all users to a new file? (y/n): ")
        if choose == "y":
            filename = input("What would you like to name the file?: ")
            with open(filename, "w", encoding="utf-8") as file:
                print(f"File {filename} has been created!")

                file.write(f"{get_all_users()}")
                break
        elif choose == "n":
            break
        else:
            print("Invalid input. Please try again.")
            return