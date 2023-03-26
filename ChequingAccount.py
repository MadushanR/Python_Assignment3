import Account
class ChequingAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, overdraftAllowed):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self.overdraftAllowed = overdraftAllowed

    def withdraw(self,amount):
        super().withdraw(self,amount)
