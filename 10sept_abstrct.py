# abstraction  : 
"""
data  hiding : it is  process of hiding the data , implementation detalis and showing only essential features of an object.
use ==>  to reduce complexity of code. and increase readability.

2  ==> class abstract  , method  ==>  abstract 

from abc import ABC  ==> abc ==> abstract base class 
==>  no  object if you declare  the class of abstract . 
"""

# class method ,  static  method  :  

"""
class person : 
    com ="PWC"
    def __init__(self):
        self.name = "arpit"
        self.age = 25
        self.gender = "male"
    def show(self):
        print("name : ",self.name)
        print("age :",self.age)
        print("gender : ",self.gender)
        print("com:",self.com)
    
    @classmethod    # decorator  ==> 
    def change_com(cls,new_com):
        cls.com = new_com
        print(cls.com)
p=person()
person.change_com("KPMG")  # direct call from class name  that is  person . 
p.change_com("KPMG")  # direct call from object  that is  person .
p.show()
"""

# static  method : 

"""
class cal():

    @staticmethod 
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
c=cal()
print(c.add(12,45))
print(c.sub(12,45))
"""
# abstraction : 

"""from abc import ABC, abstractmethod

class vehicle(ABC):   # abstract class

    @abstractmethod
    def start(self):
        pass 

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")

class bike(vehicle):
    def start(self):
        print("bike started")
    
    def stop(self):
        print("bike stopped")

c=car()
c.start()
c.stop()

b=bike()
b.start()
b.stop()
"""

# for loop  : 
"""
1.for 
2.while  
3.while True
"""
"""
syntax : 

for  variable  in range(start , end ,step):
    print()
"""
# 1-100 :
"""
for i in range(1,101):
    print(i,end= " ")

"""
# 100-1 : 
"""
for i in range(100,1,-1):
    print(i,end= " ")
"""

# start , stop  : 

"""start =int(input("enter start : "))
stop =int(input("enter stop : "))

for i in range(start,stop+1,2):
    print(i,end=" ")
"""

# prime , perfect , amg , twin  pelindorme , reverse , : 

# prime  : 2 factors : 
# perfect :  6 factors :1,2,3,6 ==>sum .= 1+2+3 =6  28 

"""n=int(input("enter the  number  :" ))
count =0 

for i in range(1,n+1):
    if n % i ==0 :
        count +=1 
if count ==2 :
    print(n,"is prime")
"""

# abstraction  : 

from abc import  ABC , abstractmethod

class bank(ABC):
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    @abstractmethod
    def deposit(self,amount):
        pass
        
    @abstractmethod
    def withdraw(self,amount):
        pass
        
    @abstractmethod
    def check_balance(self):
        pass

class savings(bank):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}")
        else :
            print(f"{self.name} does not have enough balance")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

s=savings("vyom",2500000)
s.deposit(100000)
s.withdraw(500000)
s.check_balance()