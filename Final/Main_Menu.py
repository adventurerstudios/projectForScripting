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

        if choice == "1":

        elif choice == "2":

        elif choice == "3":

        elif choice == "4":

        elif choice == "5":

        elif choice == "6":
            print("Goodbye")
            return
        else:
            print("Invalid choice, try again.")
menu()