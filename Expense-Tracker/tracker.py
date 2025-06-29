import json
import os

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_expenses(expenses):
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent = 4)

def add_expense(expenses):
    category = input("Enter the category e.g. food, transport etc: ")
    amount = float(input(" Enter their amount: "))
    expenses.append({"category":category,"amount":amount})
    save_expenses(expenses)
    print("The expenses were added!")


def view_expenses(expenses):
    # Check if the expenses list is empty
    if not expenses:
        print("No expenses found.")  # Show message if no expenses exist
        return  # Exit the function early

    total = 0  # This will store the total amount spent

    print("\nYour Expenses:")  # Print heading with a line break

    # Loop through the expenses list with index using enumerate
    for i, e in enumerate(expenses):
        # Print the number ( i+1 starting from 1), category, and amount using an f-string( which lets us insert variables directly inside the string using {}.)
        print(f"{i+1}. {e['category']} - Rs {e['amount']}") # gets category of current expense

        # Add the current amount to the total
        total = total + e['amount'] # gets amount of current expense

    # After loop, print the total amount spent with a line break before it
    print(f"\nTotal Spent: Rs {total}")

def clear_expenses():
    with open("expenses.json", "w") as file:
        json.dump([], file)
    print("All expenses have been cleared.")


def main():
    expenses = load_expenses()

    while True:
        print("\n---The Expense Tracker Menu")
        print("1.Add expense")
        print("2.View Expenses")
        print("3.clear expenses")
        print("4.Exit")
        choice = input("Enter your Choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice=="2":
            view_expenses(expenses)
        elif choice=="3":
            clear_expenses()
            expenses=[]
        elif choice=="4":
            print("Goodday!")
            break
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()

