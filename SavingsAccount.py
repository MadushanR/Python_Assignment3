import Account

class SavingsAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.minimumBalance = minimumBalance
        self.accountType = "Savings Account"


    def withdraw(self,amount):
        super().withdraw(self,amount)