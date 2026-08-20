import json 
from pathlib import Path

from expense import Expense

DATA_FILE = Path("data/expenses.json")


def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

# loading the expenses from json to python object . 
def load_expenses():
    ensure_data_file()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Expense.from_dict(item) for item in data]

    except (json.JSONDecodeError, OSError):
        return []

# Saving the expenses from python object to json.
def save_expenses(expenses):
    ensure_data_file()

    data = [expense.to_dict() for expense in expenses]

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        return False