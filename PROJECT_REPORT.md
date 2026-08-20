# PROJECT REPORT

# Personal Expense Manager

---

## 1. Problem Understanding

Managing personal income and expenses is a common everyday problem. Without a proper system, it can be difficult to understand where money is being spent, how much income has been received, and what the current balance is.

The objective of this project was to develop a functional Python application that allows users to manage financial transactions through a command-line interface.

The application needed to support transaction management, validation, searching, filtering, sorting, reporting, data persistence, and testing.

Instead of building a large or complex application, the focus was placed on creating a well-structured and understandable solution that demonstrates important Python programming concepts.

---

## 2. Objective

The main objective of the project was to build a Personal Expense Manager that allows users to:

- Record income and expense transactions
- Store transaction information persistently
- View and manage existing transactions
- Search and filter transactions
- Sort transactions
- Generate financial summaries
- Handle invalid input safely
- Demonstrate clean and modular Python programming

Another important objective was to understand the implementation completely instead of simply writing code to complete the assignment.

---

## 3. Proposed Approach

Before starting the implementation, the application was divided into separate modules based on responsibility.

The overall structure of the application is:

```text
main.py
   │
   ├── validators.py
   │
   ├── expense_service.py
   │         │
   │         └── expense.py
   │
   ├── storage.py
   │
   └── reports.py
```

Each module has a specific responsibility. This approach helps keep the application organized and avoids placing all the code inside a single file.

The development approach followed was:

```text
Understand the problem
        ↓
Analyse requirements
        ↓
Design project structure
        ↓
Implement core functionality
        ↓
Add validation
        ↓
Add data persistence
        ↓
Test functionality
        ↓
Document the project
```

---

## 4. Implementation

### 4.1 Expense Model

The `Expense` class was created to represent a single financial transaction.

Each transaction contains:

- ID
- Date
- Category
- Description
- Amount
- Transaction type

The class is also responsible for converting transaction objects into dictionaries and reconstructing objects from stored dictionary data.

This was necessary because JSON files cannot directly store custom Python objects.

The conversion process is:

```text
Expense Object
      ↓
Dictionary
      ↓
JSON File
```

When loading data:

```text
JSON File
      ↓
Dictionary
      ↓
Expense Object
```

---

### 4.2 Validation

The `validators.py` module was created to validate user input before it reaches the business logic.

The following inputs are validated:

- Amount
- Date
- Category
- Description
- Transaction type
- Transaction ID
- Menu choice

Invalid input is handled without crashing the application. Exception handling is used when converting user input into numeric values where appropriate.

---

### 4.3 Transaction Management

The `expense_service.py` module contains the main business logic.

The implemented operations include:

- Adding transactions
- Finding transactions by ID
- Updating transactions
- Deleting transactions
- Searching transactions
- Filtering transactions
- Sorting transactions

A list called `expenses` is used to store the current collection of `Expense` objects while the application is running.

```text
expenses
│
├── Expense 1
├── Expense 2
└── Expense 3
```

The same list is passed to the required functions so that they can perform operations on the current transaction data.

---

### 4.4 Data Persistence

The application uses a JSON file to store transaction data.

The `storage.py` module contains functions responsible for:

- Creating or accessing the data file as required
- Loading saved transactions
- Saving updated transactions

The file used for storage is:

```text
data/expenses.json
```

The application loads existing data when it starts and saves changes whenever transactions are added, updated, or deleted.

This ensures that data is not lost when the application closes.

---

### 4.5 Search, Filter and Sorting

The application supports searching transactions using keywords.

Transactions can also be filtered based on:

- Category
- Date
- Transaction type

Sorting functionality allows transactions to be sorted by:

- Date
- Amount

Both ascending and descending order are supported.

---

### 4.6 Financial Reports

The `reports.py` module is responsible for calculating useful financial information.

The following reports were implemented:

- Total income
- Total expenses
- Current balance
- Category summary
- Monthly summary

The balance is calculated using:

```text
Balance = Total Income - Total Expenses
```

The reporting logic was separated from the user interface so that calculations remain independent of how the results are displayed.

---

## 5. Important Technical Decisions

### Modular Project Structure

Instead of writing the complete application in `main.py`, the project was divided into separate modules. This made the code easier to understand, test, and maintain.

### Object-Oriented Design

An `Expense` class was used to represent each transaction. This allowed related transaction data to be grouped into a single object instead of managing every transaction as unrelated variables.

### JSON for Data Storage

JSON was selected because:

- It is simple to understand
- Python provides built-in support through the `json` module
- No external database is required
- It is suitable for a small application

### Passing Data Instead of Using Global State

The list of transactions is passed to functions when required instead of relying heavily on global variables.

For example:

```python
add_expense(expenses, ...)
```

This makes function dependencies explicit and keeps the business logic easier to test.

### Built-in `unittest`

Python's built-in `unittest` framework was selected for automated testing. This kept the project dependency-free and aligned with the zero-cost requirement.

---

## 6. Testing Performed

The project includes six automated unit tests.

The following scenarios were tested:

| Test Case | Scenario | Expected Result |
|---|---|---|
| Add Transaction | Add a valid transaction | Transaction is successfully added |
| Invalid Amount | Negative, zero, and text input | Input is rejected |
| Invalid Date | Impossible and incorrect date format | Input is rejected |
| Missing Transaction | Search for a non-existing ID | Returns `None` |
| Delete Transaction | Delete an existing transaction | Transaction is removed |
| Balance Calculation | Add income and expenses | Correct balance is calculated |

The tests were executed using:

```bash
python3 -m unittest discover -s tests -v
```

All six test cases completed successfully.

---

## 7. Challenges Encountered

### Understanding Data Flow Between Modules

One challenge was understanding how the list of transactions is shared between different functions.

There was initially some confusion between:

```python
expense
```

which represents a single transaction object, and:

```python
expenses
```

which represents the list containing all transaction objects.

The data flow can be understood as:

```text
Create Expense object
        ↓
Add object to expenses list
        ↓
Perform operations using the list
        ↓
Save the list to JSON
```

### JSON and Custom Objects

Another challenge was understanding why an `Expense` object cannot be directly stored inside a JSON file.

This was solved by converting objects into dictionaries before saving them and reconstructing objects when loading the data.

### Input Validation and Exception Handling

Handling invalid input required distinguishing between invalid values and values that cannot be converted to the required data type.

Both validation logic and exception handling were used to prevent invalid input from crashing the application.

### Test Discovery

During testing, the initial `unittest` command did not discover the test cases.

The issue was resolved by explicitly specifying the tests directory:

```bash
python3 -m unittest discover -s tests -v
```

After fixing the test discovery configuration, all six tests were successfully executed.

---

## 8. Solutions Implemented

The challenges encountered during development were addressed by:

- Separating the application into clear modules
- Using an `Expense` class to model transactions
- Using validation functions for user input
- Using exception handling for operations that may fail
- Converting objects to dictionaries before JSON storage
- Using helper functions for reusable operations
- Writing isolated unit tests
- Explicitly specifying the test directory for test discovery

---

## 9. Limitations

The current version of the project has several limitations:

- The application only provides a command-line interface.
- Data is stored locally in a JSON file.
- There is no authentication or multi-user support.
- The reports are text-based.
- No graphical charts are included.
- There is no budget or spending limit feature.
- The application is intended for relatively small amounts of data.

---

## 10. Future Scope

The project can be extended with several additional features:

- Graphical user interface
- SQLite or PostgreSQL database integration
- User authentication
- Multiple user accounts
- Budget management
- Spending limits and alerts
- Data visualization using charts
- Exporting reports to CSV or PDF
- Recurring transactions
- Advanced filtering
- Web or mobile application integration

---

## 11. Conclusion

The Personal Expense Manager was successfully developed as a functional Python command-line application.

The project demonstrates several important Python concepts, including object-oriented programming, modular programming, lists, dictionaries, loops, conditional logic, validation, exception handling, file handling, JSON data persistence, searching, filtering, sorting, reporting, and unit testing.

More importantly, the project provided practical experience with structuring a software project instead of writing everything in a single file.

The development process followed the basic workflow of understanding the problem, analysing the requirements, designing the structure, implementing the features, testing the functionality, and documenting the final result.

The final application is intentionally kept simple, but the structure allows additional features and improvements to be added in the future.
