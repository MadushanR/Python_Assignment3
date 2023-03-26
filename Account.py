class Account:

    def __init__(self,accountNumber,accountHolderName,currentBalance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.currentBalance = currentBalance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountHolderName(self):
        return self.accountHolderName
    
    def getCurrentBalance(self):
        return self.currentBalance
    
    def deposit(self,amount):
        self.currentBalance = self.currentBalance + amount

    def withdraw(self,amount):
        self.currentBalance = self.currentBalance - amount

    