# tuple  :  immutable  :  ordered wise 

"""
t1 =(1,2,3,4,5,"ankit","aayush")
print(t1)
print(type(t1))

t2 = 1,2,3,4,54,6,7,8,9,10
print(t2)
print(type(t2))
"""

# built in function  :  len  min  max  sorted

"""
t1 = 1,2,3,4,54,6,7,8,9,10
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sum(t1))
"""

# slicing  : 

"""
t1 = 1,2,3,4,54,6,7,8,9,10

print(t1[0])
print(t1[2 : 5])
print(t1[2 : 8 : 2])
print(t1[  :   : -1])
"""

# method  : index count  

"""
t1 = 10,20,30,40,54,6,7,8,9,10

print(t1.index(40))
print(t1.count(40)) 
"""

# tuple  convert in the list : 

t1 = 10,20,30,40,54,6,7,8,9,10

# output : (10,20,30,40,54,6,7,8,9,10 , "yash")

"""l1 = list(t1)
print(l1)
l1.append("yash")
print(tuple(l1))
"""

"""
task  : 1 

t1 =((10,20,30) , (40,50,60) , (70,80,90))
output : ((10,20,100) , (40,50,100) , (70,80,100))

"""