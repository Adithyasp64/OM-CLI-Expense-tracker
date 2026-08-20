class Expense:
    def __init__(self, expense_id, date, category, description, amount, expense_type):
        self.id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.type = expense_type

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            expense_id=data["id"],
            date=data["date"],
            category=data["category"],
            description=data["description"],
            amount=data["amount"],
            expense_type=data["type"]
        )

    def __str__(self):
        return (
            f"{self.id} | {self.date} | {self.category} | "
            f"{self.description} | ₹{self.amount:.2f} | {self.type}"
        )