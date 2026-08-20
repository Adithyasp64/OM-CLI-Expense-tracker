from expense import Expense
from storage import load_expenses, save_expenses
from validators import *
from reports import *
from expense_service import *










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

# Getting the choice from the use
def get_menu_choice():
    while True:
        choice = input("Enter your choice: ").strip()

        if validate_menu_choice(choice):
            return int(choice)

        print("Invalid choice. Please enter a number between 1 and 8.")


# Handling the transaction flow control 
def handle_add_expense(expenses):
    print("\n--- Add Transaction ---")

    # Date
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()

        if validate_date(date):
            break

        print("Invalid date. Please use DD-MM-YYYY.")

    # Category
    print("\nAvailable categories:")
    print(", ".join(ALLOWED_CATEGORIES))

    while True:
        category = input("Enter category: ").strip()

        if validate_category(category):
            category = category.title()
            break

        print("Invalid category. Please choose from the available categories.")

    # Description
    while True:
        description = input("Enter description: ").strip()

        if validate_description(description):
            break

        print("Description cannot be empty.")

    # Amount
    while True:
        amount = input("Enter amount: ").strip()

        if validate_amount(amount):
            amount = float(amount)
            break

        print("Invalid amount. Please enter a positive number.")

    # Transaction type
    while True:
        expense_type = input("Enter type (income/expense): ").strip()

        if validate_expense_type(expense_type):
            expense_type = expense_type.lower()
            break

        print("Invalid type. Enter 'income' or 'expense'.")

    # Create transaction
    expense = add_expense(
        expenses,
        date,
        category,
        description,
        amount,
        expense_type
    )

    # Save data
    if save_expenses(expenses):
        print("\nTransaction added successfully!")
        print(expense)
    else:
        print("\nTransaction was added, but could not be saved.")


# Displaying the trasaction 
def display_expenses(expenses):
    if not expenses:
        print("\nNo transactions found.")
        return

    print("\n--- Transactions ---")

    for expense in expenses:
        print(expense)

# handlging the view transaction . 
def handle_view_expenses(expenses):
    all_expenses = get_all_expenses(expenses)
    display_expenses(all_expenses)

# updating the transcation .
def handle_update_expense(expenses):
    print("\n--- Update Transaction ---")

    expense_id = input("Enter transaction ID: ").strip()

    if not validate_id(expense_id):
        print("Invalid ID.")
        return

    expense_id = int(expense_id)

    expense = find_expense(expenses, expense_id)

    if expense is None:
        print("Transaction not found.")
        return

    print("\nCurrent transaction:")
    print(expense)

    print("\nEnter new values.")

    while True:
        date = input("Date (YYYY-MM-DD): ").strip()

        if validate_date(date):
            break

        print("Invalid date.")

    print("\nAvailable categories:")
    print(", ".join(ALLOWED_CATEGORIES))

    while True:
        category = input("Category: ").strip()

        if validate_category(category):
            category = category.title()
            break

        print("Invalid category.")

    while True:
        description = input("Description: ").strip()

        if validate_description(description):
            break

        print("Description cannot be empty.")

    while True:
        amount = input("Amount: ").strip()

        if validate_amount(amount):
            amount = float(amount)
            break

        print("Invalid amount.")

    while True:
        expense_type = input("Type (income/expense): ").strip()

        if validate_expense_type(expense_type):
            expense_type = expense_type.lower()
            break

        print("Invalid type.")

    updated_expense = update_expense(
        expenses,
        expense_id,
        date,
        category,
        description,
        amount,
        expense_type
    )

    if updated_expense:
        if save_expenses(expenses):
            print("\nTransaction updated successfully!")
        else:
            print("\nTransaction updated, but could not be saved.")

# delete an expense . 
def handle_delete_expense(expenses):
    print("\n--- Delete Transaction ---")

    expense_id = input("Enter transaction ID: ").strip()

    if not validate_id(expense_id):
        print("Invalid ID.")
        return

    expense_id = int(expense_id)

    expense = find_expense(expenses, expense_id)

    if expense is None:
        print("Transaction not found.")
        return

    print("\nTransaction to delete:")
    print(expense)

    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    if delete_expense(expenses, expense_id):
        if save_expenses(expenses):
            print("Transaction deleted successfully!")
        else:
            print("Transaction deleted, but could not be saved.")


# search and filter transactions .
def handle_search_filter(expenses):
    print("\n--- Search / Filter ---")
    print("1. Search by keyword")
    print("2. Filter by category")
    print("3. Filter by date")
    print("4. Filter by type")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        keyword = input("Enter keyword: ").strip()
        results = search_expenses(expenses, keyword)

    elif choice == "2":
        category = input("Enter category: ").strip()

        if not validate_category(category):
            print("Invalid category.")
            return

        results = filter_expenses(
            expenses,
            category=category
        )

    elif choice == "3":
        date = input("Enter date (DD-MM-YYYY): ").strip()

        if not validate_date(date):
            print("Invalid date.")
            return

        results = filter_expenses(
            expenses,
            date=date
        )

    elif choice == "4":
        expense_type = input(
            "Enter type (income/expense): "
        ).strip()

        if not validate_expense_type(expense_type):
            print("Invalid type.")
            return

        results = filter_expenses(
            expenses,
            expense_type=expense_type
        )

    else:
        print("Invalid choice.")
        return

    display_expenses(results)



# Sort transactions.
def handle_sort_expenses(expenses):
    print("\n--- Sort Transactions ---")
    print("1. Sort by Date")
    print("2. Sort by Amount")

    choice = input("Choose sorting method: ").strip()

    if choice == "1":
        sort_by = "date"

    elif choice == "2":
        sort_by = "amount"

    else:
        print("Invalid choice.")
        return

    order = input(
        "Ascending or descending? (a/d): "
    ).strip().lower()

    if order == "a":
        descending = False

    elif order == "d":
        descending = True

    else:
        print("Invalid order.")
        return

    sorted_expenses = sort_expenses(
        expenses,
        sort_by=sort_by,
        descending=descending
    )

    display_expenses(sorted_expenses)

# Handling the reports section. 
def handle_reports(expenses):
    print("\n" + "=" * 45)
    print("             FINANCIAL REPORT")
    print("=" * 45)

    total_income = calculate_total_income(expenses)
    total_expenses = calculate_total_expenses(expenses)
    balance = calculate_balance(expenses)

    print(f"Total Income:   ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Balance:        ₹{balance:.2f}")

    print("\n--- Category Summary ---")

    category_summary = get_category_summary(expenses)

    if category_summary:
        for category, amount in category_summary.items():
            print(f"{category}: ₹{amount:.2f}")
    else:
        print("No data available.")

    print("\n--- Monthly Summary ---")

    monthly_summary = get_monthly_summary(expenses)

    if monthly_summary:
        for month, amount in monthly_summary.items():
            print(f"{month}: ₹{amount:.2f}")
    else:
        print("No data available.")







# running the app with all the functions . 
def run_app():
    expenses = load_expenses()

    print("\nWelcome to Personal Expense Manager!")

    while True:
        display_menu()

        choice = get_menu_choice()

        if choice == 1:
            handle_add_expense(expenses)

        elif choice == 2:
            handle_view_expenses(expenses)

        elif choice == 3:
            handle_update_expense(expenses)

        elif choice == 4:
            handle_delete_expense(expenses)

        elif choice == 5:
            handle_search_filter(expenses)

        elif choice == 6:
            handle_sort_expenses(expenses)

        elif choice == 7:
            handle_reports(expenses)

        elif choice == 8:
            print("\nThank you for using OM Expense Manager!")
            break


if __name__ == "__main__":
    run_app()