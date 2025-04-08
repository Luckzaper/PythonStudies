balance = 1000

print("Welcome!")
print(f"You have ${balance} in your account.")

while True:
    print("\nMenu")
    print("0 – Make a deposit")
    print("1 – Make a withdrawal")
    print("2 – Display account value")

    selection = input("\nPlease make a selection: ")

    if selection == '0':
        deposit_amount = float(input("How much would you like to deposit?: "))
        balance += deposit_amount
        print(f"Your current balance is ${balance}")

    elif selection == '1':
        withdraw_amount = float(input("How much would you like to withdraw?: "))

        if withdraw_amount > balance:
            print("Not enough balance. Withdrawal cancelled.")
        else:
            balance -= withdraw_amount
            print(f"Your current balance is ${balance}")

    elif selection == '2':
        print(f"Your current balance is ${balance}")

    else:
        print("Invalid entry, please try again.")

    return_to_menu = input("Would you like to return to the main menu (Y/N)?: ")

    if return_to_menu.lower() != 'y':
        print("Thank you for banking with us!")
        break