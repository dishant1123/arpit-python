# polymorphsim  : many forms  
"""
1.  method  over  loading  
2. method  over  riding  
"""
# method  over loading  with default  arg  : 

"""class calculator :
    def add(self,a=10,b=10,c=10):
            return  a+b+c       
    
c=calculator()
print(c.add())  #default args 
print(c.add(1,2))
print(c.add(10,20,30))
"""

# over riding  : 

"""class animal : 
    def speak(self):
        print("animal can speak")

class dog(animal):
    def speak(self):
        print("dog can speak")

class cat(animal):
    def speak(self):
        print("cat can speak")

c=cat()
c.speak()

"""

# loading +riding  : 

"""class shape: 
    def area(self,a=0,b=0):  # method  over  loading with default arg  
        return a*b

class square(shape):
    def area(self, a=0, b=0):  # method  over  riding
        return a*a
    
class rectangle(shape):
    pass 

s=square()
r=rectangle()

print("square area is ",s.area(4,5))  # overriding
print("rectangle area is ",r.area(4,5)) # inherited 
"""

# bank using  poly  : 

class bank :
    def __init__(self,name):
        self.name=name
        self.balance=0
    
    def deposit(self,amt,bonus=0):
        self.balance+=amt +bonus
        print(f"deposited {amt} to {self.name} account +{bonus}")
        print(f"balance is {self.balance}")

class savings(bank):
    def deposit(self, amt, bonus=0):
        interest=amt*0.05 
        self.balance+=interest +bonus  # selfbal =self.bala +int +bonus
        print(f"deposited {amt} to {self.name} account +{bonus} + int :{interest}")
        print(f"balance is {self.balance}")

# acc1=bank("vyom")   # loading  
# acc1.deposit(1000)
# acc1.deposit(2000,5000)

sav=savings("yash")  # laoding + riding  
# sav.deposit(10000)
sav.deposit(20000,5000)
