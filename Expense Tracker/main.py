
import random

#add expense with description and amount
def adding_expense(list, expense, description, id=""):
    number = random.randint(1, 100)
    list.append({"amount": expense, "description": description, "id": number})
    print(f"\nExpense successfully added (ID:{number})")
    return list

#update expense
def update_expense(list, expense, id):
    for item in list:
        if item["id"] == id:
            item["amount"] = expense
    return list


#delete expense
def delete_expense(list, id):
    for item in list:
        if item["id"] == id:
            list.remove(item)
    return list

#view all expenses
def display_expense(list):
    sorted_list = sorted(list, key=lambda item: item["id"])
    for item in sorted_list:
        print(f"ID:{item['id']} | Amount: ${item['amount']} | Description: {item['description']}")

#view summary of all expenses
def categorised_expenses(list, description):
    total_cost = 0
    for items in list:
        if items["description"].lower() == description.lower():
            total_cost += int(items["amount"])
    print(f"Total cost of {description}: {total_cost}")




list = []

def main():
    print("\nExpense Tracker")
    print("1. Add an expense")
    print("2. Update an expense")
    print("3. Delete an expense")
    print("4. Display an expense")
    print("5. Exit")

while True:
    main()
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Thank you for using this program")
        break
    elif choice == 1:
        expense = int(input("\nEnter an expense: "))
        description = str(input("Enter an expense description: "))
        adding_expense(list, expense, description)
    elif choice == 2:
        id = int(input("\nEnter an expense ID: "))
        expense = int(input("Enter an expense amount: "))
        update_expense(list, expense, id)
    elif choice == 3:
        id = int(input("\nEnter an expense ID: "))
        delete_expense(list, id)
    elif choice == 4:
        display_expense(list)
        by_category = input("\nDo you want to display the total for a decription/category (y/n): ")
        if by_category == "y":
            description = input("What category would you like to see: ")
            categorised_expenses(list, description)
        if by_category == "n":
            continue

