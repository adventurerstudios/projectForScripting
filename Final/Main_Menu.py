import requests

from user_data import *
from StealthScrape import scraper
from Export import *
def menu (): #the main function
    while True: #while loop for main function
        print("\nChoose one of the following: "
              "\n1. Create an account"
              "\n2. Log in"
              "\n3. View users"
              "\n4. Check for leaks"
              "\n5. Import/Export data"
              "\n6. Scrape"
              "\n7. Quit")
        choice = input("What would you like to do?: ")

        if choice == "1": #code for creating an account
            print(add_user(input("Enter username: "),input("Enter email: "),  input("Enter password: ")))
        elif choice == "2": #code for loging in
            print(get_user_info(input("Enter username: ")))
        elif choice == "3": #code for getting all user names
            print(get_all_users())
        elif choice == "4": #code for leak checking
            website = input("Enter URL to check for leaks: ")
            if not website.startswith("http://") and not website.startswith("https://"):
                website = "https://" + website
            try:
                response = requests.get(website)
                if response.status_code == 200:
                    leaks = check_for_leaks(response.text)
                    if leaks:
                        print("Potential leaks found:")
                        for user, email in leaks:
                            print(f"Username: {user}, Email: {email}")
                    else:
                        print("No leaks found.")
                else:
                    print(f"Failed to retrieve site. Site may not exist or is not accessible")
            except Exception as e:
                print(f"Error while checking leaks: {e}")
        elif choice == "5": #code for importing/exporting data
            action = input("Would you like to 'export' or 'import' data?: ").strip().lower()
            if action == "export":
                export()
            elif action == "import":
                filename = input("Enter the filename to import from: ").strip()
                import_data(filename)
            else:
                print("Invalid choice. Please enter 'export' or 'import'.")
        elif choice == "6": #Scraper
            scraper(input("Enter website URL: "))
        elif choice == "7": #quit function
            print("Goodbye")
            return
        else:
            print("Invalid choice, try again.")
            return
menu() #calls main function



