"""
1. single  level  inheritance  
2. multiple  level  inheritance 
3. multi level inheritance 
4. hirearchy inheritance 
5. hybrid inheritance  
"""

# single  level inheritance : 
"""class arpit :
    def __init__(self,name,age):
        self.name =name   # default  public ==> name ,age 
        self.age =age

class clg(arpit):
    def __init__(self, name, age,clg_name):
        super().__init__(name, age)
        # arpit.__init__(self,name,age)  
        self.clg_name =clg_name 
    
    def show(self): 
        print("name : ",self.name)
        print("age : ",self.age)
        print("clg_name : ",self.clg_name)
c=clg("arpit",20,"LJ")
c.show()
"""
# multi ple  level inheritance : 
"""class arpit : 
    def __init__(self):
        self.name  ="arpit"
        self.age =20

class clg :
    def __init__(self):
        self.clg ="LJ"

class teacher(arpit,clg):
    def __init__(self,t_name):
        arpit.__init__(self)
        clg.__init__(self)
        self.t_name =t_name
    
    def show(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("clg : ",self.clg)
        print("t_name : ",self.t_name)
        
t=teacher("prof.vyas")
t.show()
"""

# multi level inheritance :

"""class vehicle : 
    def __init__(self):
        self.name ="2 wheeler"
        self.price =100000 

class bike(vehicle):
    def __init__(self,model):
        super().__init__()
        self.model =model
    def show(self):
        print("name : ",self.name)
        print("price : ",self.price)
        print("model : ",self.model)

class r_one_five(bike):
    def __init__(self, model,CC):
        super().__init__(model)
        self.CC =CC
    def show(self):
        print("name : ",self.name)
        print("price : ",self.price)
        print("model : ",self.model)
        print("CC : ",self.CC)

# r=r_one_five("r one five",200)
# r.show()

b=bike("R12")
b.show()
"""

# hirearchy inheritance :  mmultiple dervired class inherit  from same base class 


