transactions = []

def add_transaction():
    date = input("Enter date: ")
    item = input("Enter item: ")
    cost = float(input("Enter cost: $"))
    transactions.append([date, item, cost])
    print("Transaction added.")

def list_transactions():
    if not transactions:
        print("No transactions.")
    else:
        for i, t in enumerate(transactions, 1):
            print(f"{i}. Date: {t[0]}, Item: {t[1]}, Cost: ${t[2]:.2f}")

def delete_transaction():
    list_transactions()
    if transactions:
        index = int(input("Enter number to delete: ")) - 1
        if 0 <= index < len(transactions):
            del transactions[index]
            print("Transaction deleted.")
        else:
            print("Invalid number.")

def total_spent():
    total = sum(t[2] for t in transactions)
    print(f"Total spent: ${total:.2f}")

while True:
    print("\nMoney Tracker")
    print("1. Add transaction")
    print("2. List transactions")
    print("3. Delete transaction")
    print("4. Show total spent")
    print("5. Quit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_transaction()
    elif choice == '2':
        list_transactions()
    elif choice == '3':
        delete_transaction()
    elif choice == '4':
        total_spent()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")