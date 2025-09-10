#oop  : 
"""
1. inheritance  : 
    a.single inheritance
    b.multiple inheritance
    c.multi level inheritance
    d. hierarchical inheritance
    e.hybrid inheritance

2. polymorphism :
    a. method overriding
    b. method overloading
3. encapsulation :
    a. get method 
    b. set method
4. abstraction
"""
# constructor  :  automatically called when object is created

"""
1. default constructor  
2. parameterized constructor
3. non parameterized constructor
4. overloading constructor
"""

# default constructor  :
"""
class person :
    def __init__(self):  # def ==> keyword , __init__ ==> method name / constructor 
        print("default constructor ,called")
        print("kirtan - jainam class")
p=person()
"""    
# non -parameterized constructor :

"""
class person : 
    def __init__(self):   
        self.name ="kirtan"  # name age clg : parameter /data member 
        self.age =20
        self.clg ="LJ NEW"
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("clg :",self.clg)
p=person()
p.show()
print(p.name)
print(p.age)
print(p.clg)
"""

# parameterized constructor :

"""class person :
    def __init__(self,name,age,clg):
        self.name =name 
        self.age =age
        self.clg =clg
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("clg :",self.clg)

name=input("enter the name : ")
age=int(input("enter the age : "))
clg=input("enter the clg_name : ")
p=person(name,age,clg)
p.show()
"""

# overloading  constructor :

"""
class person: 
    def __init__(self,name):
        self.name =name
        print("name :",self.name)

    def __init__(self,age,clg):
        self.age =age
        self.clg =clg
        print("age :",self.age)
        print("clg :",self.clg)
        
p=person(20,"lj new")
"""

# encapsulation  : 
"""
1. get method : 
2. set method :
"""

"""class person :
    def __init__(self,name,age):
        self.name =name
        self.age =age
    
    def get_name(self):
        return self.name 

    def get_age(self):
        return self.age
    def set_age(self,new_age):
        self.age =new_age
    
    # def show(self):
    #     print("name :",self.name)
    #     print("age :",self.age)

p=person("kirtan",20)
print("before using set age method")
print(p.get_name())
print(p.get_age())

print("after using set age method")
p.set_age(23)
print(p.get_name())
print(p.get_age())
"""
# private : 
class person :
    def __init__(self,name,age):
        self.__name =name   # __name ,__age ==> private
        self.__age =age
    
    def get_name(self):
        return self.__name 

    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        self.__age =new_age
    

p=person("kirtan",20)
print(p.get_name())
print(p.get_age())

p.set_age(23)
print(p.get_age())
