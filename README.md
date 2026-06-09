# Personal Finance Tracker

## Project Description

Personal Finance Tracker is a Python application that helps users manage and track their expenses. Users can add expenses, categorize spending, search records, save data to files, and generate financial reports.

This project combines concepts learned in Weeks 1–4, including variables, functions, lists, classes, file handling, JSON storage, error handling, and modular programming.

---

## Features

* Add new expenses
* View all expenses
* Search expenses
* Generate monthly reports
* Save expense data to JSON files
* Load saved expense data
* Categorize expenses
* Error handling for file operations
* User-friendly menu system

---

## Project Objectives

The main objectives of this project are:

1. Practice file handling using JSON.
2. Learn modular programming with multiple files.
3. Store and manage expense records.
4. Generate useful financial reports.
5. Apply error handling techniques.
6. Create a complete Python application.

---

## Project Structure

```text
week4-finance-tracker/
│
├── finance_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── expense.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   └── reports.py
│
├── data/
│   └── expenses.json
│
├── README.md
└── run.py
```

---

## Setup Instructions

### Requirements

* Python 3.x

### Installation

1. Download or clone the project.
2. Open Terminal or Command Prompt.
3. Navigate to the project folder.

```bash
cd week4-finance-tracker
```

4. Run the application.

```bash
python run.py
```

---

## How to Use

### Add Expense

Enter:

* Date
* Amount
* Category
* Description

Example:

```text
Date: 2026-06-09
Amount: 250
Category: Food
Description: Pizza
```

### View Expenses

Displays all stored expenses.

### Search Expenses

Search expenses using keywords from descriptions.

### Generate Report

Shows total expenses recorded.

### Save Data

Stores expense records in the JSON file.

---

## Code Structure Explanation

### expense.py

Contains the Expense class used to store expense information.

### expense_manager.py

Manages expense records, including:

* Adding expenses
* Viewing expenses
* Searching expenses

### file_handler.py

Handles:

* Saving expenses to JSON
* Loading expenses from JSON
* Error handling for files

### reports.py

Generates financial reports and calculates total spending.

### main.py

Contains the menu system and user interaction logic.

### run.py

Starts the application.

---

## Technical Requirements Completed

* Variables and Data Types
* User Input and Output
* Functions
* Classes and Objects
* Lists
* File Handling
* JSON Storage
* Error Handling
* Search Functionality
* Reports Generation
* Modular Programming
* Context Managers (`with open()`)

---

## Sample Output

```text
========================
PERSONAL FINANCE TRACKER
========================

1. Add Expense
2. View Expenses
3. Search Expenses
4. Generate Report
5. Save Data
0. Exit

Choice: 1

ADD EXPENSE

Date: 2026-06-09
Amount: 250
Category: Food
Description: Pizza

Expense Added!
```

---

## Screenshots

Add screenshots here after testing the application.

### Screenshot 1

Main Menu

### Screenshot 2

Adding Expense

### Screenshot 3

Viewing Expenses

### Screenshot 4

Generating Report

---

## What I Learned

Through this project, I learned:

* File handling in Python
* JSON data storage
* Error handling
* Modular programming
* Object-oriented programming
* Report generation
* Organizing larger Python projects

---

## Future Improvements

* Budget tracking
* CSV export
* Expense editing
* Graphical charts
* Database integration
* User login system

---

## Author

Created as part of the Week 4 Python Programming Project.

Personal Finance Tracker
