#numpy  : use  ==> array  manupulation  + matrix  , list ==> faster  
import numpy as np 

"""l1 =[1,2,3,4,5,6,7,"arpit",9j] 
print(l1) 
print(type(l1))

l1[4]="vyom"
print(l1)

"""
# l1=[[1,2,3],[4,5,6],[7,8,9]]  
# 
"""
[[1, 2, 3], 
  [4,5,6], 
   [7,8,9] ]
"""
"""print(l1)
for i in l1 : 
    print(i)
"""

"""
a=np.array([1,2,3,4,5,6,7,8,9,"arpit",9j])  # default  ==> string 
print(a)

b=np.array([1,2,3,4,5,6,7,8,9,78.90],dtype=int)  #
print(b) 

c=np.array([12.45,67.89,23.56,78],dtype=float)
print(c)
"""
# 2d array : 

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
"""
[[1 2 3]    ==> 1 2 3 ==> 1 row  ==> index 0 
 [4 5 6]    ==> 4 5 6 ==> 2 row  ==> index 1
 [7 8 9]]   ==> 7 8 9 ==> 3 row  ==> index 2
"""
"""print(a[0])
print(a[1][1])
print(a[1:3][1])
"""
"""b= np.array([[1,2,3],[4,5,6],[7,8,9]]).reshape(3,3)
print(b)
"""
# arange(): 
"""
c =np.arange(10)  # 1d 
print(c)

d= np.arange(1,21,2).reshape(2,5)
print(d)
"""

#task  :1 
"""
[[1 2 3 4 5], 
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25],
[26,27,28,29,30]] 

ouput  : [[24,25],
          [29,30]]
"""