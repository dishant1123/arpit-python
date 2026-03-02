# abtraction  : 
"""
hiding  :  hiding  the  implementation  details  of  a  class  or  method 

1. abstract  base class ==> from ABC  import abc ==> abstract basr class 
2. abstract  method  ==> decorator  ==> @abstarct method 

abstract  class or method ==> you can't create object of abstract class or method
"""
from abc import ABC , abstractmethod 

"""class vehicle (ABC):
    def engine(self):
        pass 

class car(vehicle):
    def engine(self):
        print("engine of car")

class bike(vehicle):
    def engine(self):
        print("engine of bike")

class truck(vehicle):
    def engine(self):
        print("engine of truck")

c=car()
b=bike()
t=truck()

c.engine()
b.engine()
t.engine()

"""

# using  constructor  : 

class bank(ABC):
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance =balance
    @abstractmethod
    def  deposit(self,amount):
        pass

    @abstractmethod
    def  withdraw(self,amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class SBI(bank):
    def __init__(self, name, accno,branch,balance):
        super().__init__(name, accno,balance)
        self.branch=branch
    
    def deposit(self, amount):
        self.balance +=amount
        print(f"deposited {amount} in {self.name} account")
    
    def withdraw(self, amount):
        self.balance -=amount
        print(f"withdraw {amount} from {self.name} account")

    def check_balance(self):
        print(f"balance of {self.name} account is {self.balance}")
s=SBI("arpit",122344555,"Vastrapur",25000)
s.deposit(1000)
s.withdraw(500)
s.check_balance()
