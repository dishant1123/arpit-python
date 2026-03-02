# class -object : 
"""
class ==> bule  of print  of object. 
object ==> instance  of class . 

ex : 

fruits  ==>class  
    apple kiwi banana  chiku  ==> objects 

class type  : 
1. public  : accessible  from any where 
2. private : accessible  from inside class/ within class 
3. protected : accessible  from inside class/ within class  and from inherited class
 
"""

"""
class person:  # person is class  
    def show(self):   # show ()  ==> function  / method #self ==> keyword ==> member , func access 
        print("hello")

p=person()  # p ==> is  object of class person
p.show()
"""

# data member :  

'''
class person : 
    name ="arpit"  # name  age  clg  ==> data member  ==> by default  public  
    age =20 
    clg ="LJ OLD"

"""
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("clg :",self.clg)
"""
p=person()
# p.show()
print("name : ",p.name)
print("age :",p.age)
print("clg :",p.clg)
'''

# private : class  members ==> private  ==> only within class access . 

"""class person : 
    __name =input("enter the  name : ")
    __age=int(input("enter the age : "))
    __clg =input("enter the clg_name : ")
    
    def show(self):
        print("name :",self.__name)
        print("age :",self.__age)   
        print("clg :",self.__clg)
p=person()
# print(p.__name) # error bcz of  private you can't access outside the class.
# print(p.__age) # error bcz of  private you can't access outside the class.
# print(p.__clg) # error bcz of  private you can't access outside the class.
p.show()
"""

# bank  : 

class bank : 
    name_of_account_holder =input("enter the name of account holder : ")
    account_number =int(input("enter the account number : "))
    balance =25000 

    def verify_account_number(self,accno):
        return self.account_number==accno

    def deposit(self,amt,accno):
        if self.verify_account_number(accno):
            self.balance =self.balance +amt
            print("amt deposit  successfully",amt)
            print("after deposit amt  your balance is  :",self.balance)
        else :
            print("not valid account number")
    def withdraw(self,amt,accno):
        if self.verify_account_number(accno):
            if self.balance -amt >10000 : 
                self.balance =self.balance -amt
                print("amt withdraw successfully",amt)
                print("after withdraw amt  your balance is  :",self.balance)
            else :
                print("not enough balance beacuse your maintain balance  is 10000.")
        else :
            print("not valid account number")
    def check_balance(self,accno):
            if self.verify_account_number(accno):
                print("your final balance is  :",self.balance)
    
    def show(self,accno):
        if self.verify_account_number(accno):
            print("name of account holder :",self.name_of_account_holder)
            print("account number :",self.account_number)
            print("balance :",self.balance)
        else:
            print("not valid account number")

acc_no=int(input("re-enter the account number for  verification : "))
b=bank()
print("---------SBI BANK ACCOUNT------------")
b.show(acc_no)
b.deposit(10000,acc_no)
b.withdraw(5000,acc_no)
b.check_balance(acc_no)

#1.name of account holder ,  account  number , balance  ==> private  
#2.ac number verify  ==> yes deposit  with draw check_balance  no  ==> sry   
