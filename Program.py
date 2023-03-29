import Bank

class Program():

        Bank.Bank.generateAccounts()

def showAccountMenu():
    try:
     print("\nEnter 1 to check balance ")
     print("Enter 2 to deposit ")
     print("Enter 3 to withdraw ")
     print("Enter 4 to go back to main menu ")
     print("Enter 5 to see all accounts ")
     choice = int(input("\nEnter the choice "))
     if choice == 1 :
        try:
          accountNumber = int(input("Enter account number "))
          while accountNumber <= 0:
             accountNumber = int(input("Enter valid account number "))
          Bank.Bank.searchAccount(accountNumber)
          showAccountMenu()
        except:
         print("\nEnter a valid input")
         showAccountMenu()
     elif choice == 2:
         try:
             accountNumber = int(input("Enter account number "))
             while accountNumber <= 0:
              accountNumber = int(input("Enter valid account number "))
             Bank.Bank.deposit(accountNumber)
             showAccountMenu()
         except:
          print("\nEnter a valid input")
          showAccountMenu()
     elif choice == 3:
         try:
             accountNumber = int(input("Enter account number "))
             while accountNumber <= 0:
              accountNumber = int(input("Enter valid account number "))
             Bank.Bank.withdraw(accountNumber)
             showAccountMenu()
         except:
          print("\nEnter a valid input")         
          showAccountMenu()
     elif choice == 4:
         showMainMenu()
     elif choice == 5:
         Bank.Bank.display()
         showAccountMenu()
     else:
         print("\nEnter a valid choice")
         showAccountMenu()
    except:
        print("\nEnter a valid choice")
        showAccountMenu()



def showMainMenu():
    try:
     print("\nEnter 1 to open an account ")
     print("Enter 2 to select an account ")
     print("Enter 3 to exit \n")
     choice = int(input("Enter the choice "))
     if choice == 1:
         Bank.Bank.openAccounts()
         showMainMenu()
     elif choice == 2:
         showAccountMenu()
     elif choice == 3:
         print("\nThank you")
     else:
         print("\nEnter a valid choice ")
         choice = int(input("Enter the choice "))
         showMainMenu()
    except:
        print("\nEnter a valid choice ")
        showMainMenu()

showMainMenu()


    





