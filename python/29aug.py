class bank :
    def __init__(self,name,balance):
        self.name =name 
        self.balance = balance
    
    # method  overloading with default  arg : 
    def depsoit(self,amt,source="cash"):
        print(f"Depositing {amt} in {source}")
        self.balance += amt

    # method overriding : 
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance -= amt
            print(f"Withdrawing {amt}")
        else :
            print("Insufficient funds")
    def display(self):
        print(f"Name : {self.name} \nBalance : {self.balance}")

class savingaccount(bank):
    def withdraw(self, amt):
        if amt  >= 10000 :
            print("withdraw limit exceeded for saving account")
        elif amt <= self.balance:
            self.balance -= amt
            print(f"Withdrawing {amt}")
        else :
            print("Insufficient funds")

class cuurentaccount(bank):
    def withdraw(self,amt):   # overdraft  
        overdraft_limit =5000 
        if amt <= self.balance + overdraft_limit:
            self.balance -= amt
            print(f"Withdrawing {amt}")

        else :
            print("Insufficient funds")

print("Welcome to the bank")
acc1=savingaccount("yash",15000)
acc2 = cuurentaccount("arpit",5000)

acc1.depsoit(1000)
acc1.depsoit(2000,"cheque")

acc1.withdraw(12000)
acc2.withdraw(7000)

acc1.display()
acc2.display()


