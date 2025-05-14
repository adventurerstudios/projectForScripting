from user_data import *
from StealthScrape import scraper
from Export import *
def menu ():
    while True:
        print("\nChoose one of the following: "
              "\n1. Create an account"
              "\n2. Log in"
              "\n3. View users"
              "\n4. Check for leaks"
              "\n5. Import/Export data"
              "\n6. Scrape"
              "\n7. Quit")
        choice = input("What would you like to do?: ")

        if choice == "1":
            print(add_user(input("Enter username: "), input("Enter password: "),input("Enter email: ")))
        elif choice == "2":
            print(get_user_info(input("Enter username: ")))
        elif choice == "3":
            print(get_all_users())
        elif choice == "4":
            print("Work in Progress")
        elif choice == "5":
            get_all_users()
            export()
        elif choice == "6":
            scraper(input("Enter website: "))
        elif choice == "7":
            print("Goodbye")
            return
        else:
            print("Invalid choice, try again.")
            return
menu()