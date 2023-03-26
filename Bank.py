import Account,random,SavingsAccount,ChequingAccount
class Bank(Account.Account):
    global accountList 
    accountList = []


    def __init__(self,accountNumber,accountHolderName,currentBalance):
        super().__init__(accountNumber,accountHolderName,currentBalance)

    def generateAccounts():
        n = 0
        for n in range(5) :
            accountNames = ["Peter","Sam","Andy","Amy","Stark"]
            accountBalance = [5000.0,2000.0,3022.0,2000.11,9999.69]
            minimumBalance = [500,1000,600,500,3000]
            accountNumber = random.randrange(1,1000)
            account = SavingsAccount.SavingsAccount(accountNumber,accountNames[n],accountBalance[n],minimumBalance[n])
            accountList.append(account)
        for n in range(5) :
            accountNames = ["Jack","Harry","Doja","Selena","Zayn"]
            accountBalance = [1000.0,3000.0,11000.0,7683.0,5000.05]
            overdraft = [1000,5000,10000,4000,2500]
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
        else:
            accountNumber = random.randrange(1,1000)
            accountHolderName = input("\nEnter account holder name ")
            currentBalance = float(input("Enter current balance "))  
            overDraft = float(input("Enter the overdraft amount "))
            account = ChequingAccount.ChequingAccount(accountNumber,accountHolderName,currentBalance,overDraft)
            accountList.append(account)
            print("\nAccount created ")
        Bank.display()

    def display():
        print("\nAccount Number    |Account Holder Name|Current Balance|Account Type")
        for i in accountList:
            print("| ",i.accountNumber,"             |",i.accountHolderName, "           |",i.currentBalance,"      |",i.accountType)

    def searchAccount(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                print("Acocunt number is : ",i.accountNumber," Account holder name is : ",i.accountHolderName, " and current balance is : ",i.currentBalance)
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
                    if (i.currentBalance - (i.minimumBalance +amount))>= 0:
                     Account.Account.withdraw(i,amount)
                     print("Transaction successful and current balance is : ",i.currentBalance)
                    else:
                        print("You cannot process the request as it exceeds the minimum balance, current balance is :",i.currentBalance, " and the minimum balance required is ",i.minimumBalance)
                else:
                    if ((i.currentBalance + i.overdraftAllowed) - amount)>= 0:
                     Account.Account.withdraw(i,amount)
                     print("Transaction successful and current balance is : ",i.currentBalance)
                    else:
                        print("You cannot process the request as it exceeds the overdraft, current balance is :",i.currentBalance, " and the overdraft is ",i.overdraftAllowed)  
                found = True
        if found == False:
                print("Invalid Account")