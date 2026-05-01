# Simple Expense Tracker
expenses = []

while True:
    print("\n1. Add expense  2. View total  3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        expenses.append({"category": category, "amount": amount})
        print("✓ Added")

    elif choice == "2":
        total = sum(e["amount"] for e in expenses)
        print(f"Total: ${total:.2f}")

    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.")
