# inheritance : 
"""
to inherit property of parent class 

type : 

1. single inheritance
2. multiple inheritance
3. multi level inheritance
4. hybrid inheritance
5. hirearchy level inheritance
"""

# 1 . single  inheritance :  1 base class , 1 derived class 

"""class student :  # base class 
    def __init__(self):
        self.name = "arpit jain"
        self.age = 20
        self.clg ="LJ"
    
class teacher(student):  # derived class
    def __init__(self,teachername):
        self.teachername = teachername
        student.__init__(self)
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is ",self.clg)
        print("teacher name is  :",self.teachername)

t=teacher("Vandan vyas")
print("before changing  :")
t.show()
"""

# 2 . multiple inheritance :  2 base class , 1 derived class
"""
class a 

class b  

class c (a,b): 
"""

"""class student :
    def __init__(self):
        self.name = "arpit jain"
        self.age = 20

class teacher: 
    def __init__(self):
        self.t_name="Vandan vyas"

class parent:
    def __init__(self):
        self.p_name ="prakash"

class clg(student,teacher,parent):
    def __init__(self,clg_name):
        self.clg_name =clg_name
        student.__init__(self)
        teacher.__init__(self)
        parent.__init__(self)
    
    def show(self):
        print("name is  :",self.name)
        print("father name is  :",self.p_name)
        print("age is  :",self.age)
        print("teacher name is  :",self.t_name)
        print("clg is ",self.clg_name)


c=clg("LJ")
c.show()
"""

# multi level  inheritance :  
"""
class a 

class b(a): 

class c (b): 
"""
class child :
    def __init__(self,name):
        self.name=name
        self.hobbies=[]
    def enter_hobby(self):
        print(f"enter hobby of {self.name}")
        for i in range(2):
            hobby=input("enter hobby : ")
            self.hobbies.append(hobby)
    def show(self):
        print(f"hobby {self.hobbies}")
        print(f"child of {self.name}")
class parent(child):
    def __init__(self, name):  # base class constructor calling 
        super().__init__(name) 
        # gradparent.__init__(self,name)
        self. skills=[]    # empty list 
    def enter_skill(self):
        print(f"enter skill of {self.name}")
        for i in range(2):
            skill=input("enter skill : ")
            self.skills.append(skill)
    def show(self):
        super().show()  # base class 
        print(f"skill {self.skills}")
        print(f"parent of {self.name}")

class grandparent(parent):
    def __init__(self, name):
        super().__init__(name) 
        self.friends= []

    def enter_friend(self):
        print(f"enter friend of {self.name}")
        for i in range(2):
            friend=input("enter friend : ")
            self.friends.append(friend)
    
    def show(self):
        super().show()
        print(f"friends {self.friends}")
        print(f"grandparent of {self.name}")

g=grandparent("rameshdada")
g.enter_skill()
g.enter_hobby()
g.enter_friend()
g.show()

