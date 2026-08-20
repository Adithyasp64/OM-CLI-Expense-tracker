# Personal Expense Manager

A simple command-line based Personal Expense Manager built using Python.

The application allows users to record income and expenses, manage existing transactions, search and filter records, sort transactions, generate financial summaries, and store data persistently using a JSON file.

The main goal of this project was to apply core Python concepts in a practical application while following a basic software development process: understanding the problem, designing the solution, implementing the features, testing the application, and documenting the work.

---

## Problem Statement

Managing daily expenses manually can become difficult, especially when there is no simple way to keep track of income, spending, and the remaining balance.

The objective of this project is to build a Python application that allows users to manage their financial transactions from the command line.

The application should allow users to:

- Add income and expense transactions
- View all transactions
- Update existing transactions
- Delete transactions
- Search and filter transactions
- Sort transactions
- Generate financial reports
- Save data so that it is available even after restarting the application

---

## Features

### Transaction Management

- Add a new income or expense transaction
- Automatically generate transaction IDs
- View all saved transactions
- Update an existing transaction
- Delete a transaction with confirmation

### Validation

The application validates important user inputs such as:

- Valid transaction date
- Positive amount
- Allowed category
- Non-empty description
- Valid transaction type (`income` or `expense`)
- Valid transaction ID
- Valid menu selection

Invalid input is handled without crashing the application.

### Search and Filter

Transactions can be:

- Searched using keywords
- Filtered by category
- Filtered by date
- Filtered by transaction type

### Sorting

Transactions can be sorted by:

- Date
- Amount

Both ascending and descending order are supported.

### Financial Reports

The application can generate:

- Total income
- Total expenses
- Current balance
- Category-wise summary
- Monthly summary

### Data Persistence

All transactions are stored in a JSON file.

When the application starts, previously saved transactions are loaded automatically.

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Python `json` module
- Python `pathlib` module
- Python `datetime` module
- Python `unittest` framework

No external libraries are required.

---

## Project Structure

```text
OM-expense-tracker/
│
├── data/
│   └── expenses.json
│
├── tests/
│   ├── __init__.py
│   └── test_expense_manager.py
│
├── expense.py
├── expense_service.py
├── validators.py
├── storage.py
├── reports.py
├── main.py
├── README.md
└── PROJECT_REPORT.md
```

### Module Description

| File | Responsibility |
|---|---|
| `main.py` | Handles the CLI menu and user interaction |
| `expense.py` | Defines the `Expense` class |
| `expense_service.py` | Contains transaction-related business logic |
| `validators.py` | Handles input validation |
| `storage.py` | Loads and saves transaction data using JSON |
| `reports.py` | Generates financial summaries and reports |
| `tests/` | Contains automated unit tests |
| `data/expenses.json` | Stores transaction data persistently |

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd OM-expense-tracker
```

### 3. Run the application

```bash
python3 main.py
```

No additional packages need to be installed.

---

## How to Use

After starting the application, the user will see a menu similar to this:

```text
=============================================
       PERSONAL EXPENSE MANAGER
=============================================

1. Add Transaction
2. View All Transactions
3. Update Transaction
4. Delete Transaction
5. Search / Filter Transactions
6. Sort Transactions
7. View Reports
8. Exit
```

The user can select an option and follow the instructions displayed in the terminal.

---

## Example Workflow

### Adding a Transaction

```text
Enter date: 2026-08-20
Enter category: Food
Enter description: Lunch
Enter amount: 150
Enter type: expense
```

The transaction is validated, converted into an `Expense` object, added to the list of transactions, and saved to the JSON file.

---

## Data Storage

Transaction data is stored in:

```text
data/expenses.json
```

Example:

```json
[
    {
        "id": 1,
        "date": "2026-08-20",
        "category": "Food",
        "description": "Lunch",
        "amount": 150.0,
        "type": "expense"
    }
]
```

When the application starts, the JSON data is converted back into Python `Expense` objects.

---

## Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

The tests cover:

1. Adding a transaction
2. Invalid amount handling
3. Invalid date handling
4. Searching for a missing transaction
5. Deleting a transaction
6. Calculating the account balance

### Run the tests

From the project root directory:

```bash
python3 -m unittest discover -s tests -v
```

Expected result:

```text
Ran 6 tests

OK
```

---

## Concepts Demonstrated

This project uses several important Python concepts:

- Functions and modular programming
- Object-Oriented Programming
- Classes and objects
- Lists and dictionaries
- Conditional statements
- Loops
- Exception handling
- Input validation
- File handling
- JSON serialization and deserialization
- Search, filtering, and sorting
- Data persistence
- Unit testing

---

## Limitations

The current version has a few limitations:

- The application uses a command-line interface only.
- Data is stored in a local JSON file.
- There is no user authentication.
- Transactions cannot currently be filtered using multiple conditions from the CLI at the same time.
- The application does not include graphical charts or visual reports.

---

## Future Improvements

Some possible improvements include:

- Building a graphical user interface
- Adding SQLite or another database
- Adding user authentication
- Supporting multiple users
- Adding budget limits
- Adding monthly spending goals
- Adding data visualization and charts
- Exporting reports to CSV or PDF
- Adding recurring expenses
- Adding advanced filtering options

---

## Learning Outcomes

This project demonstrates how a Python application can be structured into separate modules instead of placing all logic in a single file.

It also provides practical experience with object-oriented programming, input validation, exception handling, JSON file storage, business logic separation, reporting, and automated testing.

The project follows the complete development process of understanding a problem, designing a solution, implementing features, testing the application, and documenting the final project.

---

## Author

**Adithya S Poojary**

Python Project – Learn Depth Machine Learning Internship, Track 1
