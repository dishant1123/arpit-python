class bank :
    def __init__(self,name,accno,balance):
        self.__name =name 
        self.__accno = accno
        self.__balance = balance

    def get_name(self):
        return self.__name
    
    def set_balance(self,new_balance):
        self.__balance = new_balance
    
    def deposit(self,amount):
        self.__balance += amount
        print("after  deposit  amt  : ",self.__balance)
    
    def withdraw(self,amount):
        self.__balance -= amount
        print("after  withdraw amt  : ",self.__balance)

    def show(self):
        print(self.__name)
        print(self.__accno)
        print(self.__balance)

b=bank("kirtan",12345,25000)
print("before using set balance  : ")
b.deposit(1000)
b.withdraw(15000)
b.show()

print("after using set balance  : ")
b.set_balance(50000)
b.deposit(10000)
b.withdraw(25000)
b.show()