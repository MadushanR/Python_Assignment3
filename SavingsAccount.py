import Account

class SavingsAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)

    def withdraw(self,amount):
        super().withdraw(self,amount)