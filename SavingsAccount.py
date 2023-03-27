import Account

class SavingsAccount(Account.Account):

    def __init__(self, accountNumber, accountHolderName, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.minimumBalance = minimumBalance
        self.accountType = "Savings Account"


    def withdraw(self,amount):
        if (self.currentBalance - (self.minimumBalance +amount))>= 0:
            Account.Account.withdraw(self,amount)
            print("Transaction successful and current balance is : ",self.currentBalance)
        else:
            print("You cannot process the request as it exceeds the minimum balance, current balance is :",self.currentBalance, " and the minimum balance required is ",self.minimumBalance)