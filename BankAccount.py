class BankAccount:
    def __init__(self,name=None,typ=None,balance=None,crbalance=None):
        self._name=name
        self._typ=typ
        self._balance=balance
        self._current=crbalance
        
    def inputs(self):
        self._name=input("Enter your name:")
        self._typ=input("Enter your account type:")
        self._balance=float(input("Enter your account balance:"))

    def withdraw(self):
        self._wdamt = float(input("Enter withdraw amount:"))
        if  self._wdamt + 2000 < self._balance :
            self._current = self._balance-self._wdamt
        else:
            print("Transaction cannot performed")
            self._current=self._balance
    
    def deposit(self):
        self._deposit = float(input("enter deposit amount:"))
        self._current = self._balance + self._deposit

    def show(self):
        print()
        print("Name:",self._name)
        print("Account type:",self._typ)
        print("Account balance:",self._balance)
        print("Current balance:",self._current)
ob=BankAccount()
ob.inputs()
ob.withdraw()
ob.show()