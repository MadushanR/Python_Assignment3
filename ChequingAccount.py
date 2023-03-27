import Account
class ChequingAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, currentBalance, overdraftAllowed):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.overdraftAllowed = overdraftAllowed
        self.accountType = "Chequing Account"

    def withdraw(self,amount):
        if ((self.currentBalance + self.overdraftAllowed) - amount)>= 0:
            Account.Account.withdraw(self,amount)
            print("Transaction successful and current balance is : ",self.currentBalance)
        else:
            print("You cannot process the request as it exceeds the overdraft, current balance is :",self.currentBalance, " and the overdraft is ",self.overdraftAllowed)  
