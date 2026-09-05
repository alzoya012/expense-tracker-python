import json

expenses = []

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\nYour Expenses:")

        for i in range(len(expenses)):
            print("\nExpense", i + 1)
            print("Name:", expenses[i]["name"])
            print("Amount:", expenses[i]["amount"])
            print("Category:", expenses[i]["category"])

def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)

def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses()

    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses):
        expenses.pop(number - 1)
        save_expenses()
        print("Expense deleted successfully!")
    else:
        print("Invalid expense number!")

load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")