import Account,random
class Bank(Account.Account):
    global accountList 
    accountList = []


    def __init__(self,accountNumber,accountHolderName,currentBalance):
        super().__init__(accountNumber,accountHolderName,currentBalance)

    def generateAccounts():
        n = 0
        accountNames = ["Peter","Sam"]
        accountBalance = [5000.0,2000.0]
        for n in range(2) :
            accountNumber = random.randrange(1,1000)
            account = Bank(accountNumber,accountNames[n],accountBalance[n])
            accountList.append(account)

    def openAccounts():
        n = 0
        accountNumber = random.randrange(1,1000)
        accountHolderName = input("\nEnter account holder name ")
        currentBalance = float(input("Enter current balance "))
        account = Bank(accountNumber,accountHolderName,currentBalance)
        accountList.append(account)
        print("\nAccount created ")
        Bank.display()

    def display():
        print("\n")
        for i in accountList:
            print(i.accountNumber," ",i.accountHolderName, " ",i.currentBalance)

    def searchAccount(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                print(i.accountNumber," ",i.accountHolderName, " ",i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")

    def deposit(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                amount = int(input("Enter the amount "))
                Account.Account.deposit(i,amount)
                print(i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")


    def withdraw(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                amount = int(input("Enter the amount "))
                Account.Account.withdraw(i,amount)
                print(i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")