from StealthScrape import scraper
from user_data import get_all_users
def menu ():
    while True:
        print("\nChoose one of the following: "
              "\n1. Create an account"
              "\n2. Log in"
              "\n3. Check for leaks"
              "\n4. Import/Export data"
              "\n5. Scrape"
              "\n6. Quit")
        choice = input("What would you like to do?: ")

        if choice == "5":
            get_all_users()
        else:
            break

menu()