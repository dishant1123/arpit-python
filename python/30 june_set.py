"""
11. Write a Python program to find the indexes of numbers in a given list below a given threshold.
Original list:
[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold: 100
Check the indexes of numbers of the said list below the given threshold:
[0, 1, 2, 3, 7, 8, 9, 10]
"""

"""
l1 = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold=  100
l2 = []
for i in  l1 : 
    if i <Threshold:
       l2.append(l1.index(i)) 
print(l2)
"""
#set : mutable   ==>  unordered collection of unique elements  ==> unique => not allowed in duplicate. 


"""s1 ={1,2,3,4,5,6,7,8,"yash", "anuj", 10 , 10 , 2 }
print(s1)
print(type(s1))
"""
# empty  set : 

"""
s2 =set()
print(s2)
print(type(s2))
"""

# built in function  :  len  min  max  sorted
"""
s1 ={1,2,3,4,5,6,7,8, 100 , 10 , 25 }
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sum(s1))

"""
# slicing  :  not  allowed in set 

"""
s1 ={1,2,3,4,5,6,7,8, 100 , 10 , 25 }
print(s1[0])
"""
# method  : 
# s1 ={12,1,2,3,4,5,6,7,8, 100 , 10 , 25 }

"""
s1.add(150)
print(s1)

s1.clear()
print(s1)
"""
"""
s2 = s1.copy()
print(s2)
"""

"""s1.pop()
print(s1)"""

"""
s1.remove(102)
print(s1)
"""
"""
s1.discard(120)
print(s1)
"""

# s1={1,2,3,4}
# s2 ={2,4,90}
# s3={1,2,3,4,5,6,7,8}

"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2)) # s1 -s2 
"""

# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

s1={1,2,3,4}
s2 ={1,2,3,4,5}
s3={1,2,3,4,5,6,7,8}

# print(s1.isdisjoint(s2)) 

# print(s1.issubset(s2))

# print(s3.issuperset(s1))
# print(s3.issuperset(s2))

"""
task  : 1 
l1 = [1,2,3,4,5,5,7,8,9,9,10]
"""
l1 = [1,2,3,4,5,5,7,8,9,9,10]

print(list(set(l1)))
