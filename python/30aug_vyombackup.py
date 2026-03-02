# encapsulation  : 
"""
warapping data in single  unit . 

1. get method   : 
2 . set  method  : 
"""

# private variable :

"""class student : 
    def __init__(self,name,age):  
        self.__name =name   # __  double underscore private variable name,age 
        self.__age =age
        
    def show(self):
        print(f"name is {self.__name}")
        print(f"age is {self.__age}")

s= student("arpit",20)
s.show()
# s.__name="vyom gandhi"  not changing  bcz  of  private  
# s.__age=21
"""

# get set :  private  variable  acccess using  get and  set : 

"""class student : 
    def __init__(self,name,age):
        self.__name =name 
        self.__age =age
    def getname(self):
        return self.__name 
    def getage(self):
        return self.__age
    def setname(self,newname):
        self.__name=newname

s=student("arpit",20)
print("before using set method  : ")
print(s.getname())   # arpit 
print(s.getage())   #  age 

s.setname("vyom gandhi")
print("after using set method  : ")
print(s.getname())   
"""

"""
multi level  : 


class a : 
class b(a) : 
class c(b) :
"""

class vehicle :
    def __init__(self):
        self.name ="4 vehiler"

    def show(self):
        print(f"name is {self.name}")

class car(vehicle):
    def __init__(self,car_name,model):
        super().__init__()   # base class constructor calling
        self.car_name =car_name
        self.model =model
    
    def show(self):
        super().show()  # base class
        print(f"car name is {self.car_name}")
        print(f"model is {self.model}")

class truck(car):
    def __init__(self,truck_name,model):
        self.truck_name =truck_name
        self.model =model
    
    def show(self):
        print(f"truck name is {self.truck_name}")
        print(f"model is {self.model}")

t=truck("ashok","A123")
t.show()

c=car("audi","A4")
c.show()