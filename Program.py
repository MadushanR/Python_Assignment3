print("Enter 1 to open an account ")
print("Enter 2 to select an account ")
print("Enter 3 to exit ")
choice = int(input("Enter the choice "))

def showAccountMenu():
    print("Enter 1 to check balance ")
    print("Enter 2 to deposit ")
    print("Enter 3 to withdraw ")
    print("Enter 4 to go back to main menu ")
    choice = int(input("Enter the choice "))

if choice == 2:
    showAccountMenu()



