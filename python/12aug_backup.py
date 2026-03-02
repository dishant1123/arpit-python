# class :blue  print  
# object : instance of class  
"""
class type  : 

1.  public :  accessible from anywhere
2. private  : accessible from inside class
3. protected : accessible from inside class and sub class
""" 
"""class person : 
    def show(self):   # method / function  : self ==> class member , function ==>access from inside class
        print("arpit vyom function")
p=person()   # p object  ==> person  class name  
p.show()

"""

# data member : 

"""class person : 
    name= "arpit" # name , age  : data member   default  public 
    age =21 

    def show(self):
        print("name is  :",self.name)
        print("age is :",self.age)
p=person()
p.show()  # function call 
print(p.name)  # direct print  though object
print(p.age)
"""

# private  : 

class person :
    __name ="vyom"
    __age=21
    __clg="LJ"

    def __display(self):
        print("best friend name is arpit.")

    def show1(self):
        self.__display()

    def show(self):
        print("name is  ",self.__name)
        print("age is  ",self.__age)
        print("clg is",self.__clg)
p=person()
# print(p.__name)  # error ==> bcz private accessible  only within class 
p.show()
# p.__display()  # error ==> bcz private function  accessible  only within class
p.show1()
