# *args == > number   and **kwargs == > key value   ==> dict 

"""def s(*args):
    return sum(args)  # sum  ==> built in function  
print(s(1,2,3,4,66,88))
"""
"""def d1(**kwargs):  #takes two  arg  key value 
    for i ,  j  in kwargs.items():
        print(f'{i} : {j}')
d1(name='arpit', age=25, gender='male')
"""

# lambda function  :  one  liner  function  

"""
def big(a,b):
    if a>b :
        return a
    else :
        return b
print(big(10,12))
"""
# lambda : 
"""
syntax : 

lambda arg :  expression
"""
"""
x = lambda a ,b : max(a,b)
print(x(12,17))
"""

"""a=lambda x,y : x+y
print(a(10,20))
"""

# if else : 
"""a=lambda x ,y: print("x is big") if x >y  else print("x is small")
x =int(input("enter x"))
y =int(input("enter y"))
a(x,y)
"""

# task  :1 
"""
ask user to enter the number and seprate odd even in list  .
l1 = [1,2,3,4,5,6,6,67,7,7]
odd = []
even =[]

"""

"""n =int(input("enter the  num : "))
l2=[]

for i  in range(n):
    num = int(input("enter the num  : "))
    l2.append(num)
print(l2)

even=[]
odd=[]
for i in  l2 :
    if i % 2==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
"""

# filter  : [1,2,3,4,5,6,7,8,9] 

"""l1=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda x : x % 2 ==0,l1))
b=tuple(filter(lambda x : x % 2 ==1,l1))
print(a)
print(b)
"""
# task  : 1 
"""
input : l1 =["php","java","c","python","c++","1221"]
output  : l1= ["php","1221"]
"""

