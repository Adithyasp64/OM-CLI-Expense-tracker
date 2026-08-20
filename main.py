from expense import Expense


def display_menu():
    print("\n" + "=" * 40)
    print("    OM - PERSONAL EXPENSE MANAGER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search / Filter Expenses")
    print("6. Sort Expenses")
    print("7. View Reports")
    print("8. Exit")
    print("=" * 40)


def get_menu_choice():
    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= 8:
            return int(choice)

        print("Invalid choice. Please enter a number between 1 and 8.")


def run_app():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("\nAdd Expense selected.")

        elif choice == 2:
            print("\nView Expenses selected.")

        elif choice == 3:
            print("\nUpdate Expense selected.")

        elif choice == 4:
            print("\nDelete Expense selected.")

        elif choice == 5:
            print("\nSearch / Filter Expenses selected.")

        elif choice == 6:
            print("\nSort Expenses selected.")

        elif choice == 7:
            print("\nView Reports selected.")

        elif choice == 8:
            print("\nThank you for using Personal Expense Manager.")
            break


if __name__ == "__main__":
    run_app()