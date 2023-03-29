import Account,random,SavingsAccount,ChequingAccount
class Bank():
    global accountList 
    accountList = []


    def __init__(self,accountNumber,accountHolderName,currentBalance):
        self.account = Account.Account(accountNumber,accountHolderName,currentBalance)

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
        try:
         accountType = int(input("Enter account type \n 1.Savings Account \n 2.Chequing Account\n "))
         if accountType == 1:
             accountNumber = random.randrange(1,1000)
             accountHolderName =  input("\nEnter account holder name ")
             try:
                 currentBalance = float(input("Enter current balance ")) 
                 while currentBalance < 0:
                     currentBalance = float(input("Enter a valid value "))
             except:
                     currentBalance = float(input("Enter a valid value "))
                     while currentBalance < 0:
                         currentBalance = float(input("Enter a valid value"))
             try:
                 minimumBalance = float(input("Enter the minimum balance "))
                 while minimumBalance < 0:
                     minimumBalance = float(input("Enter a valid value "))
             except:
                     minimumBalance = float(input("Enter a valid value "))
                     while minimumBalance < 0:
                         minimumBalance = float(input("Enter a valid value"))
             account = SavingsAccount.SavingsAccount(accountNumber,accountHolderName,currentBalance,minimumBalance)
             accountList.append(account)
             print("\nAccount created ")
         elif accountType == 2:
             accountNumber = random.randrange(1,1000)
             accountHolderName = input("\nEnter account holder name ")
             try:
                 currentBalance = float(input("Enter current balance ")) 
                 while currentBalance <= 0:
                     currentBalance = float(input("Enter a valid value "))
             except:
                     currentBalance = float(input("Enter a valid value "))
                     while currentBalance <= 0:
                         currentBalance = float(input("Enter a valid value"))            
             try:
                 overDraft = float(input("Enter the overdraft amount "))
                 while overDraft <= 0:
                     overDraft = float(input("Enter a valid value "))
             except:
                     overDraft = float(input("Enter a valid value "))
                     while overDraft <= 0:
                         overDraft = float(input("Enter a valid value"))
             account = ChequingAccount.ChequingAccount(accountNumber,accountHolderName,currentBalance,overDraft)
             accountList.append(account)
             print("\nAccount created ")
         else:
              print("\nEnter a valid choice\n")
              Bank.openAccounts()
              Bank.display()
        except:
            print("\nEnter a valid choice\n")
            Bank.openAccounts()  

    def display():
        print("\nAccount Number    |Account Holder Name|Current Balance|Account Type")
        for i in accountList:
            print("| ",i.accountNumber,"             |",i.accountHolderName, "           |",i.currentBalance,"      |",i.accountType)

    def searchAccount(accountNumber):
        found = False
        for i in accountList:
            if i.accountNumber == accountNumber :
                print("Account number is : ",i.accountNumber," Account holder name is : ",i.accountHolderName, " and current balance is : ",i.currentBalance)
                found = True
        if found == False:
                print("Invalid Account")

    def deposit(accountNumber):
        try:
         found = False
         for i in accountList:
             if i.accountNumber == accountNumber :
                 account = Bank(i.accountNumber,i.accountHolderName,i.currentBalance)
                 amount = float(input("Enter the amount "))
                 while amount <= 0:
                    amount = float(input("Enter valid amount "))
                 Account.Account.deposit(i,amount)
                 print("Transaction successful and current balance is : ",i.currentBalance)
                 found = True
         if found == False:
                 print("Invalid Account")
        except :
            print("Going back to main menu due to invalid input")


    def withdraw(accountNumber):
        try:
         found = False
         for i in accountList:
             if i.accountNumber == accountNumber :
                 amount = float(input("Enter the amount "))
                 while amount <= 0:
                    amount = float(input("Enter valid amount "))
                 if i.accountType == "Savings Account":
                     SavingsAccount.SavingsAccount.withdraw(i,amount)
                 else:
                     ChequingAccount.ChequingAccount.withdraw(i,amount)
                 found = True
         if found == False:
                 print("Invalid Account")
        except :
            print("Going back to main menu due to invalid input")