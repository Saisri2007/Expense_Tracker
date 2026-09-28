import csv

FILE = "expenses.csv"

def add_expense():
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            print("\nDate\t\tCategory\tAmount")
            print("--------------------------------")

            for row in reader:
                if row:
                    print(f"{row[0]}\t{row[1]}\t\t₹{row[2]}")
    except FileNotFoundError:
        print("No expenses found.")


def total_expenses():
    total = 0

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    total += float(row[2])

        print(f"\nTotal Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
