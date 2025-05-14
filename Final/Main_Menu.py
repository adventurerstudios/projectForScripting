import requests

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
            website = input("Enter URL to check for leaks: ")
            response = requests.get(website)
            if response.status_code == 200:
                leaks = check_for_leaks(response.text)
                if leaks:
                    print("⚠️ Potential leaks found:")
                    for user, email in leaks:
                        print(f"Username: {user}, Email: {email}")
                else:
                    print("✅ No leaks found.")
            else:
                print("Failed to retrieve site.")
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

#delete
