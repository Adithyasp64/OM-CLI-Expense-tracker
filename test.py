from expense import Expense
from reports import calculate_total_income

expenses = [
    Expense(1, "2026-08-19", "Other", "Salary", 5000, "income"),
    Expense(2, "2026-08-19", "Food", "Lunch", 180, "expense"),
    Expense(3, "2026-08-19", "Other", "Freelance", 11000, "income")
]

print(calculate_total_income(expenses))