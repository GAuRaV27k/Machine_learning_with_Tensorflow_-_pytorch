class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def withdrawl(self, amount):
        print(f"your withdrawl the {amount} and remain balamce is {self.balance -amount}")

    def deposit(self, amount):
        print(f"your deposit the {amount} and current balamce is {self.balance + amount}")    
    
    def checkbalance(self):
        print(f"your current balance is {self.balance}")


Gaurav = BankAccount(2325,"Gaurav", 2000)
print(f"The account holder is {Gaurav.owner_name} with account number {Gaurav.account_number} and balance of {Gaurav.balance}")
Gaurav.withdrawl(1200)
Gaurav.deposit(5000)
Gaurav.checkbalance()