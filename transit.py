from BankAccount import BankAccount
class Transaction:
    def __init__(self,account,mode,amount):
        super().__init__()
        self.account=account
        self.mode= mode
        self.amount=amount
    
    def run(self):
        if mode==1:
            self.account.withdraw()
        elif mode==2:
            self.account.deposit()
        else 
            print()
        