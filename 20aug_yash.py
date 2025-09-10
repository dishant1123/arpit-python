# class method  : 
# @class method : decorator 

"""class student : 
    com = "PWC"

    def __init__(self):
        self.name = "arpit jain"
        self.age = 20
    
    @classmethod     
    def new_com(cls,new_com):  # cls as first parameter 
        cls.com = new_com

    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("com is ",self.com)

s=student()
s.show()
student.new_com("KPMG")  # student class 
s.show()
"""
# static method :  
# @staticmethod  : decorator 

"""
class student : 
    @staticmethod
    def sum(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b
    
s=student()
print(s.sum(12,13))
print(s.sub(12,13))
"""

# abstraction  : 
"""
hide the details of the implementation

abstract class method

@abstarct method 

from abc  import ABC ==> abc  ==> abstract base  class 
"""

from abc import ABC, abstractmethod

class bank(ABC):
    def __init__(self):
        self.name = "SBI"
        self.branch = "SBI-thaltej"
        self.balance =25000

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def check(self):
        pass
class SBI(bank):
    def __init__(self):
        super().__init__()
        self.manager = "arpit jain"
    
    def deposit(self,amt):
        self.balance +=amt
        print("balance is ",self.balance)
    
    def withdraw(self,amt):
        self.balance -=amt
        print("balance is ",self.balance)
    
    def check(self):
        print("balance is ",self.balance)
    def show(self):
        print("name is  :",self.name)
        print("branch is  :",self.branch)
        print("manager is  :",self.manager)
s=SBI()

s.show()
s.deposit(100000)
s.withdraw(10000)
s.check()