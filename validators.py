from datetime import datetime


ALLOWED_CATEGORIES = [
    "Food",
    "Transport",
    "Education",
    "Bills",
    "Shopping",
    "Entertainment",
    "Health",
    "Other"
]

ALLOWED_TYPES = [
    "income",
    "expense"
]


# validaiting the the amount , should be float , greater than 0 and need to be an integer.
def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


# validating date.
def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False



# validating the categories . 
def validate_category(category):
    return category.strip().title() in ALLOWED_CATEGORIES

# validating the description.
def validate_description(description):
    return bool(description.strip()) # returns true anything is there otherwise false using bool function . 

# Validating expense type 
def validate_expense_type(expense_type):
    return expense_type.strip().lower() in ALLOWED_TYPES

# Valdiating the id , when using the update and delete . 
def validate_id(expense_id):
    try:
        expense_id = int(expense_id)

        return expense_id > 0

    except ValueError:
        return False

# Validating the menu choice in main.py
# learning return 1 <= choice <= 8 if choice is 10 then it does not jump to except block , it just return false. 
def validate_menu_choice(choice):
    try:
        choice = int(choice)

        return 1 <= choice <= 8

    except ValueError:
        return False