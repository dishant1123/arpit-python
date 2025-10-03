# polimorphism :  many  forms 
"""
1. method overriding
2. method overloading
"""

# method  over loading with deafult  arg : 

"""
class calculator:
    
    def add(self,a=0,b=0):
        return a+b
   
    def sub(self,a=0,b=0):
        return a-b

c=calculator()
print(c.add(12,13))
print(c.sub(34,78))
"""

#method overriding :

"""class animal :
    def sound(self):
        print("animal sound")

class cat(animal):
    def sound(self):
        print("cat sound : mewwwwoooowwww")

class dog(animal):
    def sound(self):
        print("dog sound : bhowwwwoooowwbhowwww") 
        
a=[animal(),cat(),dog()]

for i in a: 
    i.sound()
"""

# method  over loading  using constructor  and *args : 

"""class student: 
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
            self.age =None
        elif len(args)==2:
            self.name=args[0]
            self.age =args[1]
        
        else :
            self.name="unknown"
            self.age=0 
            
    def display(self):
        print(f"name : {self.name} , age : {self.age}")

s=student("arpit")
s1=student("arpit",23)
s3=student("arpit",23,45)
s4=student()

# s.display()
# s1.display()
# s3.display()
# s4.display()

for i in [s,s1,s3,s4]:
    i.display()
"""

# method  over riding  using constructor  and *args :

class person:
    def __init__(self,*args,**kwargs):
        self.name=kwargs.get("name","unknown")
        self.age=kwargs.get("age",0)
        print(f"name : {self.name} , age : {self.age}")

class employee(person):
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)  # base class constructor
        self.salary=kwargs.get("salary",0)
        print(f"salary : {self.salary}")
        

p1=person(name="arpit",age=23)
print("++++++++++++++++++++++++++++++++++++++")

e=employee(name="arpit",age=23,salary=1000)
