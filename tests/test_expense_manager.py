### Here we could have used the pytest , since it requires an installation so that why I have not used it here but it makes code more cleaner than defualt python unittest . 

import unittest

from expense_service import (
    add_expense,
    find_expense,
    delete_expense
)

from validators import (
    validate_amount,
    validate_date
)

from reports import calculate_balance


class TestExpenseManager(unittest.TestCase):

    def test_add_expense(self):
        expenses = []

        expense = add_expense(
            expenses,
            "20-08-2026",
            "Food",
            "Lunch",
            150.0,
            "expense"
        )

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expense.id, 1)
        self.assertEqual(expense.amount, 150.0)


    def test_invalid_amount(self):
        self.assertFalse(validate_amount("-100"))
        self.assertFalse(validate_amount("0"))
        self.assertFalse(validate_amount("abc"))


    def test_invalid_date(self):
        self.assertFalse(validate_date("2026-02-30"))


    def test_find_missing_expense(self):
        expenses = []

        result = find_expense(expenses, 10)

        self.assertIsNone(result)


    def test_delete_expense(self):
        expenses = []

        expense = add_expense(
            expenses,
            "2026-08-20",
            "Food",
            "Lunch",
            150,
            "expense"
        )

        result = delete_expense(expenses, expense.id)

        self.assertTrue(result)
        self.assertEqual(len(expenses), 0)


    def test_calculate_balance(self):
        expenses = []

        add_expense(
            expenses,
            "20-08-2026",
            "Other",
            "Salary",
            5000,
            "income"
        )

        add_expense(
            expenses,
            "20-08-2026",
            "Food",
            "Groceries",
            1200,
            "expense"
        )

        balance = calculate_balance(expenses)

        self.assertEqual(balance, 3800)


if __name__ == "__main__":
    unittest.main()