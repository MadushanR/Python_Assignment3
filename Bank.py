import Account,random
class Bank(Account.Account):


    def __init__(self,accountNumber,accountHolderName,currentBalance):
        super().__init__(accountNumber,accountHolderName,0.5,currentBalance)

    def generateAccounts():
        n = 0
        global accountList
        accountList = []
        while n <5 :
            accountNumber = random.randrange(1,1000)
            accountHolderName = input("Enter account holder name ")
            currentBalance = float(input("Enter current balance "))
            account = Bank(accountNumber,accountHolderName,currentBalance)
            accountList.append(account)
            n = n+1

    def searchAccount(self,accountNumber):
        accountNumber = int(input("Enter account number to search"))
        accountList.index(accountNumber)
