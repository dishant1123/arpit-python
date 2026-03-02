# data type  : 
"""
1. string : immutable sequence of characters
2. list   : mutable sequence of any type
3. tuple  : immutable sequence of any type
4. dict   : mutable mapping of any type
5.  set  : mutable unordered collection of unique elements
"""

# list  : array  : mutable sequence of any type  ==>mutable ==> you can changes in list. 

"""l1=[1, 2, 3, 4, 5, "vyom", 2j, 3.14]
#   0  1  2  3  4  5       6    7 
print(l1)
print(type(l1))

# index : 0 
print(l1[0])

l1[0] ="arpit"
print(l1)
"""

# built in function : len min max sorted sum 

"""
l1=[1,2,3,4,5,6,7,8,900,23,23.45]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  #asc to dec 
print(sum(l1))
"""
# slicing  : 

"""l1=[10,20,30,40,50,60,70,80,900,23,23.45]
# 
# index : positive  => 0 ==> l to r 
# negative index : -1 ==> r to l 
print(l1[0])
print(l1[-1])
print(l1[1 : 3])  # starting  1  end 3   for  (start , stop  , step )
print(l1[2 :3])
print(l1[  : 5 ])
print(l1[ 2 :  ])
print(l1[ 2 : 8 : 2 ])
# a : 30 50 70    anu: 30 60  vyom:30 50 70 
print(l1[  :  : -2 ])
# anu   a   vyom 
print(l1[  :  : -1 ])
"""
# task  : 1 
"""
take one list  and sort list by dec to asc .
l1 = [25,6,78,99,23,1,2]
"""

# task  : 2 
"""
take a   one list  and print min and max value of list  but don't use built in function .
l1 = [25,6,78,99,23,1,2]
output  : min 1  max = 99 
"""
"""l1 = [25,6,78,99,23,1,2]

largest=l1[0]  # largest =99

for i in l1:  # 23
    if i > largest:   # 2 > 99 
        largest = i   # largest =99  
print(largest)
"""
# task  : 3 
"""
l1 = [1,4,9,23,60,11,24]
print second largest element in list  : 24
"""
l1 = [1,4,9,23,60,11,24]

l2 =sorted(l1)
print(l2)
print(l2[-2])