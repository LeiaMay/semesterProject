import csv
from datetime import datetime

class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

class PersonalFinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount, category):
        transaction = Transaction(date, description, amount, category)
        self.transactions.append(transaction)
        print("Transaction added successfully!")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions to display.")
        else:
            for idx, transaction in enumerate(self.transactions, start=1):
                print(f"{idx}. Date: {transaction.date}, Description: {transaction.description}, "
                      f"Amount: {transaction.amount}, Category: {transaction.category}")

    def calculate_summary(self):
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        print(f"Total Expenses: {total_expenses}")
        print(f"Total Income: {total_income}")

    def categorize_transactions(self):
        categories = {}
        for transaction in self.transactions:
            if transaction.category in categories:
                categories[transaction.category].append(transaction)
            else:
                categories[transaction.category] = [transaction]

        for category, transactions in categories.items():
            print(f"Category: {category}")
            for transaction in transactions:
                print(f"Date: {transaction.date}, Description: {transaction.description}, "
                      f"Amount: {transaction.amount}")

    def export_transactions_to_csv(self, filename):
        with open(filename, mode='w', newline='') as csvfile:
            fieldnames = ['Date', 'Description', 'Amount', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow({
                    'Date': transaction.date,
                    'Description': transaction.description,
                    'Amount': transaction.amount,
                    'Category': transaction.category
                })
        print(f"Transactions exported to {filename}")

    def import_transactions_from_csv(self, filename):
        try:
            with open(filename, mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.add_transaction(row['Date'], row['Description'], float(row['Amount']), row['Category'])
            print(f"Transactions imported from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error importing transactions: {e}")


def main():
    finance_tracker = PersonalFinanceTracker()

    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Summary")
        print("4. Categorize Transactions")
        print("5. Export Transactions to CSV")
        print("6. Import Transactions from CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            finance_tracker.add_transaction(date, description, amount, category)

        elif choice == '2':
            print("\n==== All Transactions ====")
            finance_tracker.view_transactions()

        elif choice == '3':
            print("\n==== Summary ====")
            finance_tracker.calculate_summary()

        elif choice == '4':
            print("\n==== Categorized Transactions ====")
            finance_tracker.categorize_transactions()

        elif choice == '5':
            filename = input("Enter filename to export (e.g., transactions.csv): ")
            finance_tracker.export_transactions_to_csv(filename)

        elif choice == '6':
            filename = input("Enter filename to import (e.g., transactions.csv): ")
            finance_tracker.import_transactions_from_csv(filename)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
