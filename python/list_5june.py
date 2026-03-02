# method  : 

l1=[1,2,3,8,9,20,25,3,3]

# l1.append(l2)
# print(l1)

# l1.clear()
# print(l1)

# l2=l1.copy()
# print(l2)

"""l2=["banana","apple","mango","orange"]

l1.extend(l2)
print(l1)
"""

# l1.insert(2,"arpit")  # index , value 
# print(l1)

# print(l1.index(3))
# print(l1.index(3,4,10)) # 3 index   start   stop 

# l1.pop(6)  # index though delete
# print(l1)

# l1.remove(3)
# print(l1)

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# print(l1.count(3))

"""
task  : 1 
ask user to enter the list element  store  in to the list  and  remove  the duplicate element.

5 = 1 2 2 3 4 
l1 = [1,2,2,3,4]

output  : 1 2 3 4
"""
"""n=int(input("enter the list element  : "))
l1 =[]

for i  in range(n):
    num =  int(input("enter the list element  : "))
    l1.append(num)
print(l1)
"""
"""l1 = [1,2,2,3,4,5,5,6,6,8,10,10]
l2=[]
for i in l1 : 
    if  i not in  l2:
        l2.append(i)
print(l2)
"""

"""
take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]
"""

"""l1=[121 , 131 , 123 ,145 , 789 ]
l2=[]
for i in l1:
    rev = 0
    temp =i
    while  temp > 0:
        r= temp % 10 
        rev = rev *10 +r 
        temp = temp //10 
    if rev ==i:
        l2.append(i)
print(l2)
"""
"""
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100),(70,80,100)]
"""
t1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# (10, 20, 40), ==> 0   ==> 10 ==> 0   
# (40, 50, 60), ==> 1  
# (70, 80, 90) ==> 2 

"""l2=[]
for i in t1 :
    t2 = i[:-1] + (100,)
    l2.append(t2)
print(l2)"""



