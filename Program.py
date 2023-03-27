import Bank

class Program(Bank.Bank):

        Bank.Bank.generateAccounts()

def showAccountMenu():
    print("\nEnter 1 to check balance ")
    print("Enter 2 to deposit ")
    print("Enter 3 to withdraw ")
    print("Enter 4 to go back to main menu ")
    print("Enter 5 to see all accounts ")
    choice = int(input("\nEnter the choice "))
    if choice == 1 :
        accountNumber = int(input("Enter account number "))
        Program.searchAccount(accountNumber)
        showAccountMenu()
    elif choice == 2:
        accountNumber = int(input("Enter account number "))
        Program.deposit(accountNumber)
        showAccountMenu()
    elif choice == 3:
        accountNumber = int(input("Enter account number "))
        Program.withdraw(accountNumber)
        showAccountMenu()
    elif choice == 4:
        showMainMenu()
    elif choice == 5:
        Program.display()
        showAccountMenu()
    else:
        print("\nEnter a valid choice")
        showAccountMenu()


def showMainMenu():
    print("\nEnter 1 to open an account ")
    print("Enter 2 to select an account ")
    print("Enter 3 to exit \n")
    choice = int(input("Enter the choice "))
    if choice == 1:
        Program.openAccounts()
        showMainMenu()
    elif choice == 2:
        showAccountMenu()
    elif choice == 3:
        print("\nThank you")
    else:
        print("\nEnter a valid choice ")
        choice = int(input("Enter the choice "))
        showMainMenu()

showMainMenu()


    





