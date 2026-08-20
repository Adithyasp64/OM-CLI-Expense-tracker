# calculating the total income . 
def calculate_total_income(expenses):
    total_income = 0

    for expense in expenses:
        if expense.type == "income":
            total_income += expense.amount

    return total_income

# Calculating the total expenses. 
def calculate_total_expenses(expenses):
    total_expense = 0

    for expense in expenses:
        if expense.type == "expense":
            total_expense += expense.amount

    return total_expense

# Balance left . 
def calculate_balance(expenses):
    total_income = calculate_total_income(expenses)
    total_expenses = calculate_total_expenses(expenses)

    return total_income - total_expenses

# category wise summary 
def get_category_summary(expenses):
    summary = {}

    for expense in expenses:
        if expense.category not in summary:
            summary[expense.category] = 0

        summary[expense.category] += expense.amount

    return summary

# Calculating monthly income 
def get_monthly_summary(expenses):
    summary = {}

    for expense in expenses:
        month = expense.date[:7:-1]

        if month not in summary:
            summary[month] = 0

        summary[month] += expense.amount

    return summary  