def generate_report(expenses):

    total = 0

    for expense in expenses:
        total += expense.amount

    print("\n===== MONTHLY REPORT =====")
    print(f"Total Expenses: ₹{total}")
    