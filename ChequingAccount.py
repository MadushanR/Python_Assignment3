import Account
class ChequingAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, currentBalance, overdraftAllowed):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.overdraftAllowed = overdraftAllowed
        self.accountType = "Chequing Account"

    def withdraw(self,amount):
        self.currentBalance = self.currentBalance + self.overdraftAllowed
        super().withdraw(self,amount)
