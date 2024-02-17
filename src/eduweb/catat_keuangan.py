cash_in_transactions = []
cash_out_transactions = []

def cash_in(amount):
    cash_in_transactions.append(amount)
    print(f"Cash in recorded: {amount}\n")

def cash_out(amount):
    cash_out_transactions.append(amount)
    print(f"Cash out recorded: {amount}\n")

def calculate_cash_in_total():
    return sum(cash_in_transactions)

def calculate_cash_out_total():
    return sum(cash_out_transactions)

def calculate_total():
    return calculate_cash_in_total() - calculate_cash_out_total()

while True:
    print("1. Cash In")
    print("2. Cash Out")
    print("3. List Cash In Transactions")
    print("4. List Cash Out Transactions")
    print("5. View Total Cash In")
    print("6. View Total Cash Out")
    print("7. View Total")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the amount for cash in: "))
        cash_in(amount)

    elif choice == '2':
        amount = float(input("Enter the amount for cash out: "))
        cash_out(amount)

    elif choice == '3':
        print("List of cash in transactions:", cash_in_transactions)

    elif choice == '4':
        print("List of cash out transactions:", cash_out_transactions)

    elif choice == '5':
        total_cash_in = calculate_cash_in_total()
        print("Total cash in:", total_cash_in)

    elif choice == '6':
        total_cash_out = calculate_cash_out_total()
        print("Total cash out:", total_cash_out)

    elif choice == '7':
        total = calculate_total()
        print("Total cash balance:", total)

    elif choice == '8':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

