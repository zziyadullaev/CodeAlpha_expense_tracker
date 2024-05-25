from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category="Uncategorized"):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append({"description": description, "amount": amount, "category": category, "date": date})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for idx, expense in enumerate(self.expenses):
                print(f"{idx + 1}. Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)
            print("Expense added.")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
