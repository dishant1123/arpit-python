import  numpy as np 
import random  

"""a=np.random.randint(high=10,low=-10,size=(3,3))
print(a)

b=np.random.random((3,3))  # random  : 0-1 float value 
print(b)

c=np.linspace(start=0,stop=9.5,num=20)  # start  , stop  , num
print(c)
"""
# formula  : 
# linespace = stop -start / num  = 9.5 - 0 /20 = 0.475

# array attributes  : 

"""
x= np.random.randint(low=-30,high=50,size=12).reshape(3,4)
print(x)
print(x.shape)
print(x.ndim)
print(x.size)
print(x.itemsize)# bytes 
print(x.nbytes)

print(x.T)  # transpose
"""

# mathematical  methods:  axis  =0 col wise  axis =1 row wise 

"""x= np.random.randint(low=-30,high=50,size=12).reshape(3,4)
print(x)
print(x.sum())
print(x.sum(axis=0))
print(x.sum(axis=1))
print(x*3)
print(x+10)
print(x-20)
print(x/10)
"""

"""
a= np.random.randint(low=0,high=10,size=9).reshape(3,3)
b= np.random.randint(low=-5,high=10,size=9).reshape(3,3)

print(a)
print(b)

print(a+b)  #element by element addition (matrix addition)
print(a*b)  # not matrix multiplication

result =np.matmul(a,b)  # matrix multiplication
print(result)

c=np.sin(a)
print(c)

d=np.sqrt(a)
print(d)
"""

# np.where() : condition 

"""
c=np.random.randint(low=-10,high=10,size=10)
print(c)
print(np.where(c>0))
"""

# count_zero() : 

c=np.random.randint(low=-10,high=10,size=10)
print(c)

# print(np.count_nonzero(c))  # count  
print(np.nonzero(c))  # index number 