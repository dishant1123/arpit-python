# inheritance : 
"""
to inherit  another class property  and method.
"""

"""class student : 
    def __init__(self):
        self.name ="yash"
        self.clg = "GLS"
    
class clg(student):
    def __init__(self,location):
        # super().__init__()  # base class constructor  called 
        student.__init__(self)
        self.location =location
    def show(self):
        print("name :",self.name)
        print("clg :",self.clg)
        print("location :",self.location)

c=clg("Ahmedabad")
c.show()
c.name="kirtan"
c.show()
"""
"""
name  , clg ==>  private   ==> get,set  ==> set  clgname : 

clg (student)
"""

# multiple  inheritance : 
"""
class a : 

class b : 

class c(a,b):
"""

"""class child: 
    def __init__(self):
        self.name ="yash"
        self.age=20 
class mother :
    def __init__(self):
        self.mother_name = "bhumi ben"
class father(child,mother) : 
    def __init__(self,father_name):
        child.__init__(self)
        mother.__init__(self)
        self.father_name =father_name
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("mother_name :",self.mother_name)
        print("father_name :",self.father_name)

f=father("nimesh")
f.show()
"""
"""
task  :1 : 

child  name  age  ==>  private   ==> get,set  ==> set  name /age  :

student  clg location  ==> private  ==> get 

clg (student , child)  ==>  name  ==> gls   ==> child  student 
"""

"""
# multi  level 
class a    # base 

class b (a) 

class c(a)

class d (a)
"""

