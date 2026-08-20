from expense import Expense



# This is for to print the next id .  Note : here expenses is list to which we appending it.    
def get_next_id(expenses):
    if not expenses:
        return 1

    return max(expense.id for expense in expenses) + 1

# TO add an expense . 
def add_expense(expenses, date, category, description, amount, expense_type):
    expense_id = get_next_id(expenses)

    expense = Expense(
        expense_id,
        date,
        category,
        description,
        amount,
        expense_type
    )

    expenses.append(expense)

    return expense


# To print all the expenses made 
def get_all_expenses(expenses):
    return expenses.copy()

# To find a particular expense , used as a module i think to update and delete
def find_expense(expenses, expense_id):
    for expense in expenses:
        if expense.id == expense_id:
            return expense

    return None 

# To update an existing expense using the id 
def update_expense(
    expenses,
    expense_id,
    date,
    category,
    description,
    amount,
    expense_type
):
    expense = find_expense(expenses, expense_id)

    if expense is None:
        return None

    expense.date = date
    expense.category = category
    expense.description = description
    expense.amount = amount
    expense.type = expense_type

    return expense

# To delete an expense . 
def delete_expense(expenses, expense_id):
    expense = find_expense(expenses, expense_id)

    if expense is None:
        return False

    expenses.remove(expense)

    return True

# To search an expense . 
def search_expenses(expenses, keyword):
    keyword = keyword.lower()

    results = []

    for expense in expenses:
        if (
            keyword in expense.description.lower()
            or keyword in expense.category.lower()
        ):
            results.append(expense)

    return results

# Filter expenses based on the cateogory ,date,type
def filter_expenses(
    expenses,
    category=None,
    date=None,
    expense_type=None
):
    results = expenses.copy()

    if category:
        results = [
            expense
            for expense in results
            if expense.category.lower() == category.lower()
        ]

    if date:
        results = [
            expense
            for expense in results
            if expense.date == date
        ]

    if expense_type:
        results = [
            expense
            for expense in results
            if expense.type.lower() == expense_type.lower()
        ]

    return results


# Sorting the expenses 
def sort_expenses(expenses, sort_by="date", descending=False):
    if sort_by == "amount":
        return sorted(
            expenses,
            key=lambda expense: expense.amount, # used the lamda function to sort based on the amount (key) in a dictionary . 
            reverse=descending
        )

    if sort_by == "date":
        return sorted(
            expenses,
            key=lambda expense: expense.date, 
            reverse=descending
        )

    return expenses.copy()