# encapsulation  :  private access directly  
"""
1 . get : get from the  data  ==> print  
2. set : new  value  set . 
"""

class bank  : 
    def __init__(self,name,accno):
        self.__name =name   # name  acc no  balance ==> private 
        self.__accno =accno
        self.__balance =25000 
        
    def deposit(self,amt):
        self.__balance +=amt 
        print(f"Deposited {amt} ")

    def withdraw(self,amt):
        self.__balance -=amt
        print(f"withdraw {amt} ")
    
    def get_name(self):
        return self.__name

    def get_accno(self):
        return self.__accno
    
    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance = new_balance

b=bank("arpit",123456)
print("=============before using set method===============")
print("name :",b.get_name())
print("accno :",b.get_accno())

b.deposit(1000)
b.withdraw(500)
print("your final balance is :",b.get_balance())
print("=============after using set method===============")

b.set_balance(100000)
b.deposit(10000)
b.withdraw(5000)
print("your final balance is :",b.get_balance())