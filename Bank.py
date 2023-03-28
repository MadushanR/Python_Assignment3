import Account,random,SavingsAccount,ChequingAccount
class Bank():
    global accountList 
    accountList = []


    def __init__(self,accountNumber,accountHolderName,currentBalance):
        super().__init__(accountNumber,accountHolderName,currentBalance)

    def generateAccounts():
        n = 0
        for n in range(2) :
            accountNames = ["Peter","Sam"]
            accountBalance = [5000.0,2000.0]
            minimumBalance = [500,1000]
            accountNumber = random.randrange(1,1000)
            account = SavingsAccount.SavingsAccount(accountNumber,accountNames[n],accountBalance[n],minimumBalance[n])
            accountList.append(account)
        for n in range(3) :
            accountNames = ["Jack","Harry","Doja"]
            accountBalance = [1000.0,3000.0,11000.0]
            overdraft = [1000,5000,10000]
            accountNumber = random.randrange(1,1000)
            account = ChequingAccount.ChequingAccount(accountNumber,accountNames[n],accountBalance[n]+overdraft[n],overdraft[n])
            accountList.append(account)

    def openAccounts():        
        accountType = int(input("Enter account type \n 1.Savings Account \n 2.Chequing Account\n "))
        if accountType == 1:
            accountNumber = random.randrange(1,1000)
            accountHolderName = input("\nEnter account holder name ")
            currentBalance = float(input("Enter current balance "))  
            minimumBalance = float(input("Enter the minimum balance "))
            account = SavingsAccount.SavingsAccount(accountNumber,accountHolderName,currentBalance,minimumBalance)
            accountList.append(account)
            print("\nAccount created ")
        elif accountType == 2:
            accountNumber = random.randrange(1,1000)
            accountHolderName = input("\nEnter account holder name ")
            currentBalance = float(input("Enter current balance "))  
            overDraft = float(input("Enter the overdraft amount "))
            account = ChequingAccount.ChequingAccount(accountNumber,accountHolderName,currentBalance,overDraft)
            accountList.append(account)
            print("\nAccount created ")
        else:
             print("\nEnter a valid choice\n")
             Account.Account.openAccounts()
        Bank.display()

    def display():
        print("\nAccount Number    |Account Holder Name|Current Balance|Account Type")
        for i in accountList:
            print("| ",i.accountNumber,"             |",i.accountHolderName, "           |",i.currentBalance,"      |",i.accountType)

    def searchAccount(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                print("Accunt number is : ",i.accountNumber," Account holder name is : ",i.accountHolderName, " and current balance is : ",i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")

    def deposit(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                amount = float(input("Enter the amount "))
                Account.Account.deposit(i,amount)
                print("Transaction successful and current balance is : ",i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")


    def withdraw(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                amount = float(input("Enter the amount "))
                if i.accountType == "Savings Account":
                    SavingsAccount.SavingsAccount.withdraw(i,amount)
                else:
                    ChequingAccount.ChequingAccount.withdraw(i,amount)
                found = True
        if found == False:
                print("Invalid Account")