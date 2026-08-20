from expense import Expense
from storage import save_expenses, load_expenses

expenses = []

expense = Expense(
    1,
    "2026-08-19",
    "Food",
    "Lunch",
    180.0,
    "expense"
)

expenses.append(expense)

print("Saving...")
print(save_expenses(expenses))

print("Loading...")
loaded_expenses = load_expenses()

for expense in loaded_expenses:
    print(expense)