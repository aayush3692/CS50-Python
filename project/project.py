amount = 0
def main():
    global amount
    while True:
        print("Welcome to BANK!! ")
        print("Select option: ")
        print("1. Show balance ")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Add account")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                show_balance()
            case '2':
                deposit_money()
            case '3':
                withdraw_money()
            case '4':
                add_account()
            case '5':
                transfer_money()
            case '6':
                exit()
                break
            case _:
                print("Invalid choice! ")

        answer = input("Do you perform another operation(yes/no)? ").strip().lower()
        if answer != 'yes':
            break
def add_account():
    with open("customers.txt", "a") as file:
        print("Enter customer information: ")
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        balance = input("Enter balance: ")
        file.write(f"{name},{acc_no},{balance}\n")

def show_balance():
        acc_num = input("Enter your account number: ")
        found = False
        with open("customers.txt", "r") as file:
            for line in file:
                name, acc_no, balance = line.strip().split(",")
                if acc_num == acc_no:
                    print(f"Name: {name}")
                    print(f"Balance: {balance}")
                    found = True
                    break
            if not found:
                print("Invalid account number. ")


def deposit_money():
    try:
        acc_num = input("Enter the acc_no: ")
        found = False
        new_line = []

        with open("customers.txt", "r") as file:
            for line in file:
                try:
                    name, acc_no, balance = line.strip().split(",")
                    balance = int(balance)  # Convert balance to integer
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                if acc_num == acc_no:
                    try:
                        money = int(input("Enter the amount to deposit: "))
                        if money < 0:
                            print("Invalid Amount")
                            continue  # Skip adding to the balance if the amount is invalid
                        else:
                            balance += money
                    except ValueError:
                        print("Invalid input! Please enter a number.")
                        continue  # Skip processing if input is not a number
                    found = True
                new_line.append(f"{name},{acc_no},{balance}")

        if not found:
            print("Account not found! ")

        with open("customers.txt", "w") as file:
            for line in new_line:
                file.write(line + "\n")

    except FileNotFoundError:
        print("Unable to open file.")

def withdraw_money():
    try:
        acc_num = input("Enter the account number: ")
        found = False
        new_lines = []

        with open("customers.txt", "r") as file:
            for line in file:
                name, acc_no, balance = line.strip().split(",")
                balance = int(balance)
                if acc_num == acc_no:
                    try:
                        money = int(input("Enter the amount to withdraw: "))
                        if money > balance:
                            print("Not enough funds")
                            continue
                        else:
                            print(f"{money} Money withdrawn")
                            balance = balance - money

                    except ValueError:
                        print("Invalid amount! ")
                        continue
                    found = True
                new_lines.append(f"{name},{acc_no},{balance}")

        if not found:
            print("Unable to proceed transaction")


        with open("customers.txt", "w") as file:
            for line in new_lines:
                file.write(line + "\n")

    except FileNotFoundError:
        print("Unable to find file. ")

def transfer_money():
    try:
        sender_acc_no = input("Enter sender account no: ")
        receiver_Acc_no = input("Enter receiver account no: ")
        money = int(input("Enter amount to transfer: "))
        new_line = []
        sender_confirm = False
        receiver_confirm = False
        with open("customers.txt", "r") as file:
            for line in file:
                name, acc_no, balance = line.split(",")
                balance = int(balance)

                if acc_no == sender_acc_no:
                    if money > balance:
                        print("Not enough funds! ")
                        continue
                    else:
                        balance -= money
                        sender_confirm = True

                if acc_no == receiver_Acc_no:
                    balance += money
                    receiver_confirm = True

                new_line.append(f"{name},{acc_no},{balance}")
        if not sender_confirm:
            print("Unable to send money. ")
        if not receiver_confirm:
            print("Unable to receive money. ")

        with open("customers.txt", "w") as file:
            for line in new_line:
                file.write(line+ "\n")
    except FileNotFoundError:
        print("File not found! ")

def exit():
    print("Thank you for using our services. ")


if __name__ == "__main__":
    main()    
