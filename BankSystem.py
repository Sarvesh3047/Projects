print("Welcome to Bank")

user_data = {}

while True:
    print("\nSelect:")
    print("1) Sign Up")
    print("2) Log In")
    print("3) Exit")

    try:
        select = int(input("Select: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")
        continue

    if select == 1:
        username = input("Enter User Name: ")
        accountnumber = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if accountnumber in user_data:
            print("Error: Account number already exists!")
        else:
            user_data[accountnumber] = {'username': username, 'pin': pin, 'balance': 0.0}
            print(f"User '{username}' Account: '{accountnumber}' signed up successfully!")

    elif select == 2:
        accountnumber = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if accountnumber in user_data and user_data[accountnumber]['pin'] == pin:
            print("Log in successful!")
            print(f"Welcome {user_data[accountnumber]['username']}, Account Number: {accountnumber}")

            while True:
                print("\nSelect:")
                print("1) Account Details")
                print("2) Debit Money")
                print("3) Transfer Money")
                print("4) Credit Money")
                print("5) Logout")

                try:
                    choice = int(input("Select: "))
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 4.")
                    continue

                if choice == 1:
                    print(
                        f"\nAccount Details:\nUsername: {user_data[accountnumber]['username']}\nAccount Number: {accountnumber}\nBalance: ₹{user_data[accountnumber]['balance']}")


                elif choice == 2:

                    amount = float(input("Enter amount to debit: ₹"))

                    while True:

                        pin_input = input("Enter your PIN: ")

                        if pin_input == user_data[accountnumber]['pin']:

                            if amount > user_data[accountnumber]['balance']:

                                print("Insufficient balance!")

                            else:

                                user_data[accountnumber]['balance'] -= amount

                                print(
                                    f"Debited ₹{amount} successfully. Remaining balance: ₹{user_data[accountnumber]['balance']}")

                            break


                        else:

                            print("Incorrect PIN!")

                            print("1) Re-enter PIN")

                            print("2) Cancel Transaction")

                            try:

                                retry_choice = int(input("Select an option: "))

                            except ValueError:

                                print("Invalid input! Please enter 1 or 2.")

                                continue

                            if retry_choice == 1:

                                continue

                            elif retry_choice == 2:

                                print("Transaction canceled.")

                                break

                            else:

                                print("Invalid choice! Please select again.")

                elif choice == 3:
                    amount = float(input("Enter amount to Transfer: ₹"))
                    transfer_account = int(input("Enter recivers account number:"))

                    while True:

                        pin_input = input("Enter your PIN: ")

                        if pin_input == user_data[accountnumber]['pin']:

                            if amount > user_data[accountnumber]['balance']:

                                print("Insufficient balance!")

                            else:

                                user_data[accountnumber]['balance'] -= amount

                                print(
                                    f"Transfer of ₹{amount} successfully. Remaining balance: ₹{user_data[accountnumber]['balance']}")

                            break


                        else:

                            print("Incorrect PIN!")

                            print("1) Re-enter PIN")

                            print("2) Cancel Transaction")

                            try:

                                retry_choice = int(input("Select an option: "))

                            except ValueError:

                                print("Invalid input! Please enter 1 or 2.")

                                continue

                            if retry_choice == 1:

                                continue

                            elif retry_choice == 2:

                                print("Transaction canceled.")

                                break

                            else:

                                print("Invalid choice! Please select again.")

                elif choice == 4:
                    amount = float(input("Enter amount to credit: ₹"))
                    user_data[accountnumber]['balance'] += amount
                    print(f"Credited ₹{amount} successfully. New balance: ₹{user_data[accountnumber]['balance']}")

                elif choice == 5:
                    print("Logging out...")
                    break

                else:
                    print("Entered option is invalid! Please try again.")

        else:
            print("Invalid account number or PIN.")

    elif select == 3:
        print("Exiting...")
        break

    else:
        print("Entered option is invalid! Please try again.")
