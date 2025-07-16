class Expense:
    def __init__(self, amount, category, note, date=None):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date or datetime.now()
 

class Finances:
    def __init__(self):
        self.expenses = []  # list of Expense objects

    def add_expense(self, amount, category, note="", date=None):
        expense = Expense(amount, category, note, date)
        self.expenses.append(expense)

    def view_expenses(self):
        for i, exp in enumerate(self.expenses):
            print(f"{i+1}. ${exp.amount:.2f} - {exp.category} - {exp.note} ({exp.date.strftime('%Y-%m-%d')})")

    def total_spent(self):
        return sum(exp.amount for exp in self.expenses)

    def filter_by_category(self, category):
        return [exp for exp in self.expenses if exp.category == category]