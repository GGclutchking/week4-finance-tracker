from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses
from finance_tracker.reports import generate_report

class FinanceTracker:

    def __init__(self):
        self.manager = ExpenseManager()

    def add_expense(self):

        print("\nADD EXPENSE")

        date = input("Date (YYYY-MM-DD): ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")

        self.manager.add_expense(
            date,
            amount,
            category,
            description
        )

        print("Expense Added Successfully!")

    def view_expenses(self):

        expenses = self.manager.get_all_expenses()

        print("\nALL EXPENSES")

        if len(expenses) == 0:
            print("No expenses found.")
            return

        for expense in expenses:
            print(
                f"{expense.date} | "
                f"₹{expense.amount} | "
                f"{expense.category} | "
                f"{expense.description}"
            )

    def search_expenses(self):

        keyword = input("Enter keyword: ")

        results = self.manager.search_expenses(keyword)

        print("\nSEARCH RESULTS")

        if len(results) == 0:
            print("No matching expenses found.")

        for expense in results:
            print(
                f"{expense.date} | "
                f"₹{expense.amount} | "
                f"{expense.category} | "
                f"{expense.description}"
            )

    def run(self):

        while True:

            print("\n==============================")
            print(" PERSONAL FINANCE TRACKER ")
            print("==============================")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Search Expenses")
            print("4. Generate Report")
            print("5. Save Data")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.search_expenses()

            elif choice == "4":
                generate_report(
                    self.manager.get_all_expenses()
                )

            elif choice == "5":
                save_expenses(
                    self.manager.get_all_expenses()
                )
                print("Data Saved Successfully!")

            elif choice == "0":
                print("Thank you for using Finance Tracker!")
                break

            else:
                print("Invalid Choice!")
                