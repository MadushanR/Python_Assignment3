import Bank

Bank.Bank.generateAccounts()
Bank.Bank.display()


def showAccountMenu():
    print("\nEnter 1 to check balance ")
    print("Enter 2 to deposit ")
    print("Enter 3 to withdraw ")
    print("Enter 4 to go back to main menu ")
    choice = int(input("\nEnter the choice "))
    if choice == 1 :
        accountNumber = int(input("Enter account number "))
        Bank.Bank.searchAccount(accountNumber)
    elif choice == 2:
        accountNumber = int(input("Enter account number "))
        Bank.Bank.deposit(accountNumber)
    elif choice == 3:
        accountNumber = int(input("Enter account number "))
        Bank.Bank.withdraw(accountNumber)
    elif choice == 4:
        run()


def run():
    print("\nEnter 1 to open an account ")
    print("Enter 2 to select an account ")
    print("Enter 3 to exit \n")
    choice = int(input("Enter the choice "))
    if choice == 1:
        Bank.Bank.openAccounts()
    elif choice == 2:
        showAccountMenu()
    elif choice == 3:
        print("\nThank you")
run()


    





