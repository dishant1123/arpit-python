"""class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
        # super().__init__()
        Test.__init__(self)
# def main():
b = Derived_Test()
print(b.x) 
print(b.y)
# main()
"""
"""
class A:
    def test1(self):
        print(" test of A called ")
class B(A):
    def test(self):
        print(" test of B called ")
class C(A):
    def test(self):
        print(" test of C called ")
class D(C):
    def test2(self):
        print(" test of D called ")        
obj=D()
obj.test()"""

"""class Demo:
    def __init__(self):
        self.x = 1
    def change(self):
        self.x = 10

class Demo_derived(Demo):
    def change(self):
        self.x=self.x+1
        print(self.x)

obj = Demo_derived()
obj.change()
"""

import numpy as np 

"""a=np.array([[1,2,3,
             4,5,6,
             7,8,9]],dtype=int)
print(a)
print(type(a))
print(np.ndim(a))

b=np.array(34)
print(b)
"""

"""b=np.array([[
    [1,2,3],
    [4,5,6]],
    [[7,8,9],
    [10,11,12]
]])
print(b)
print(b[0,1,2])
print(b[1,1,2])
"""

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(2,3,2)
# print(a)

"""arr1 = np.array([[1, 2], [3, 4]])
print(arr1)
arr2 = np.array([[5, 6], [7, 8]])
print(arr2)
arr = np.concatenate((arr1, arr2), axis=1)  # row 
arr3 = np.concatenate((arr1, arr2), axis=0)  # col 

print(arr)
print(arr3)
"""

"""arr1 = np.array([[[1, 2], [3, 4]]])
arr2 = np.array([[[5, 6], [7, 8]]])
"""
# print(arr1)
# print(arr2)
# arr = np.concatenate((arr1, arr2), axis=0)
"""arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
"""
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
  
[[[1 2]
 [3 4]
 [5 6]
 [7 8]]]
"""

"""arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
"""
"""arr = np.array([[1, 2], [3, 4], [5, 4]])
print(arr)

x =np.where(arr == 4)
print(x)
"""
"""A=np.array([[[1,2], [4,3]], [[3,5], [6,4]]])
print(A)
x=np.where(A==4)
print(x)"""

"""class employee :
    def __init__(self):
        self.name =""
        self.salary =0 
        
    def input(self):
        self.name = input("Enter name : ")
        self.salary = int(input("Enter salary : "))
        
    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        
class manager(employee):
    def __init__(self):
        super().__init__()
        self.m_name =""
    
    def input(self):
        super().input()
        self.m_name = input("Enter manager name : ")
    
    def display(self):
        # super().display()
        employee.display(self)
        print("Manager name : ",self.m_name)
m=manager()
m.input()
m.display()
"""

"""class employee :
    def __init__(self,name,salary):
        self.name =name
        self.salary =salary
            
    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        
class manager(employee):
    def __init__(self,name,salary,m_name):
        super().__init__(name,salary)
        self.m_name =m_name
    
    def display(self):
        # super().display()
        employee.display(self)
        print("Manager name : ",self.m_name)
m=manager("arpit",10000,"dr.vyom")
m.display()
"""

# pip install matplotlib.pyplot 
"""
plt.figure()
plt.title() 
plt.xlabel() 
plt.ylabel()
plt. plot() ==> line graph 
plt.bar() ==> bar graph
plt.hist() ==> histogram
plt.scatter() ==> scatter plot
plt.pie() ==> pie chart
plt.boxplot() ==> box plot

"""
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[2,6,5,15,17,19,9]

plt.plot(x,y,marker='d',color='red')
# plt.bar(x,y)
plt.title("BAR Graph")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.show()
