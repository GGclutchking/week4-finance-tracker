import json
import os

FILE_NAME = "data/expenses.json"

def save_expenses(expenses):
    data = []

    for expense in expenses:
        data.append(expense.to_dict())

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print("Error saving file:", e)

def load_expenses():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except Exception as e:
        print("Error loading file:", e)
        return []
    