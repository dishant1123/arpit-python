# hirechical inheritance :  base class 1 ==>muliple derived class inherit from same base class.

"""
class a
class b(a) :
class c (a)
"""
"""
class vehicle : 
    def __init__(self):
        self.name ="4 vehiler"
    def show(self):
        print(f"name is {self.name}")
class car(vehicle):
    def __init__(self,car_name,model):
        super().__init__()
        self.car_name =car_name
        self.model =model
    def show(self):
        print(f"car name is {self.car_name}")
        print(f"model is {self.model}")
        vehicle.show(self)   # base class
class truck(vehicle):
    def __init__(self,truck_name,model):
        super().__init__()
        self.truck_name =truck_name
        self.model =model
    def show(self):
        print(f"truck name is {self.truck_name}")
        print(f"model is {self.model}")
        vehicle.show(self)   # base class    
t=truck("ashok","A123")
t.show()
"""

# hybrid inheritance :  it is  combination of more than one type of inheritance.

class a :
    def feature_a(self):
        print("feature a from a class ")
class b(a):
    def feature_b(self):
        print("feature b from b class ")
class d(a):
    def feature_d(self):
        print("feature d from d class ")
class c(b,d):
    def feature_c(self):
        print("feature c from c class ")

obj_b=b()
obj_d=d()
obj_c=c()

print("from class b")
obj_b.feature_a()
obj_b.feature_b()

print("from class d")
obj_d.feature_a()
obj_d.feature_d()

print("from class c")
obj_c.feature_a()
obj_c.feature_b()
obj_c.feature_d()
obj_c.feature_c()

#  multi level  :     vs  multiple inheritance
"""
class a :                class a :
class b(a) :             class b: 
class c(b) :            class c(a,b) :

"""
