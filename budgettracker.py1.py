import json
from collections import defaultdict

class BudgetTracker:
    def __init__(self):
        self.transactions = defaultdict(list)

    def add_transaction(self, transaction_type, category, amount):
        self.transactions[transaction_type].append({"category": category, "amount": amount})

    def calculate_budget(self):
        total_income = sum(transaction['amount'] for transaction in self.transactions['income'])
        total_expenses = sum(transaction['amount'] for transaction in self.transactions['expense'])
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def analyze_expenses(self):
        expense_categories = defaultdict(int)
        for expense in self.transactions['expense']:
            expense_categories[expense['category']] += expense['amount']
        return expense_categories

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.transactions = json.load(file)

def main():
    budget_tracker = BudgetTracker()

    # Load existing data if available
    try:
        budget_tracker.load_data('transactions.json')
    except FileNotFoundError:
        pass

    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_transaction('income', category, amount)
            print("Income added successfully.")

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_transaction('expense', category, amount)
            print("Expense added successfully.")

        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: {remaining_budget}")

        elif choice == '4':
            expense_analysis = budget_tracker.analyze_expenses()
            print("Expense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: {amount}")

        elif choice == '5':
            budget_tracker.save_data('transactions.json')
            print("Data saved successfully.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
