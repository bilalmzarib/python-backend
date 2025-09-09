import json
import os
from datetime import datetime


DATA_FILE = "data.json"

class Transaction:
    def __init__(self, amount, category, trans_type, date=None):
        self.amount = amount
        self.category = category
        self.trans_type = trans_type  # "income" or "expense"
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.trans_type,
            "date": self.date
        }

class Ledger:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        t = Transaction(
                            amount=item['amount'],
                            category=item['category'],
                            trans_type=item['type'],
                            date=item['date']
                        )
                        self.transactions.append(t)
            except Exception as e:
                print("❌ Error loading data:", e)

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)

    def add_transaction(self, amount, category, trans_type, date=None):
        t = Transaction(amount, category, trans_type, date)
        self.transactions.append(t)
        self.save_data()
        print("✅ Transaction added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print(" No transactions recorded yet.")
            return
        print("\n📋 All Transactions:")
        print("-" * 50)
        for t in self.transactions:
            print(f"[{t.date}] {t.trans_type.upper():<7} | {t.category:<15} | ${t.amount:.2f}")
        print("-" * 50)

    def show_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.trans_type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.trans_type == "expense")
        balance = total_income - total_expense
        print("\n📊 Financial Summary:")
        print("-" * 30)
        print(f"💰 Total Income:    ${total_income:.2f}")
        print(f"💸 Total Expenses:  ${total_expense:.2f}")
        print(f"🧮 Net Balance:     ${balance:.2f}")
        print("-" * 30)

def main_menu():
    ledger = Ledger()
    while True:
        print("\n========= Expense Tracker CLI =========")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1' or choice == '2':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., Salary, Rent): ")
                date = input("Enter date (YYYY-MM-DD) or leave empty: ")
                if date:
                    # validate date
                    datetime.strptime(date, "%Y-%m-%d")
                trans_type = "income" if choice == '1' else "expense"
                ledger.add_transaction(amount, category, trans_type, date if date else None)
            except ValueError:
                print("❌ Invalid amount or date format.")
            except Exception as e:
                print("❌ Error:", e)

        elif choice == '3':
            ledger.view_transactions()

        elif choice == '4':
            ledger.show_summary()

        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main_menu()
