import Account

class SavingsAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self.minimumBalance = minimumBalance


    def withdraw(self,amount):
        super().withdraw(self,amount)