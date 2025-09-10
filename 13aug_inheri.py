# constructor  : 
"""
it is automatically call when we create object  of  class. 

type : 
1. default constructor
2. parameterized constructor
3. non-parameterized constructor
4. constrcutor overloading  

"""
# default constructor : 

"""class student: 
    def __init__(self):  #def keyword , __init__ ==> constrcutor ,special method 
        print("arpit jain")
        print("vyom gandhi")

s=student()
"""

# non parameterized constructor :

"""
class student : 
    def __init__(self):
        self.name = "arpit jain"
        self.age = 20
        self.clg ="LJ"
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is ",self.clg)
s=student() 
s.show()
print(s.name)
print(s.age)
print(s.clg)
"""

# parameterized constructor :

"""
class student :
    def __init__(self,name,age,clg):
        self.name =name
        self.age =age
        self.clg =clg
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is ",self.clg)

s=student("arpit jain",20,"LJ")
s.show()
# print(s.name)
# print(s.age)
# print(s.clg)
"""

# over loading  constructor : 

class student : 
    def __init__(self):
        self.name = "arpit jain"
        self.age = 20
        self.clg ="LJ"
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is ",self.clg)
class clg:
    def __init__(self):
        self.name = "vyom gandhi"
        self.age = 21
        self.clg ="LG"
    
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is ",self.clg)

# s=student()
# s.show()
s=student()
c=clg()
c.show()
s.show()
