# for loop  : 
"""
syntax : 

for variable  in range(start,end,step):
    print(variable)
"""
# 1-100 : 
"""
for i in range(1,101):
    print(i,end=" ")
"""
# 100- 1 : 
"""for x in  range(100 , 0,-1):
    print(x,end=" ")
"""

# 1-100 even  : 

"""
for  i in range(2,100,2):
    print(i,end=" ")
""" 

"""
l1 =[1,2,3,4,5,6,7,8,"yash"]
# index  start : 0    l  to r 
# neg index start : -1    r  to  l 
print(l1[0])
print(l1[-1])

for  i in  l1 : 
    print(i,end=" ")
"""
# user  input  for : 

"""
n=int(input("enter the num : "))
for  i in range(1,n+1):
    print(i,end=" ")
""" 

l1 =[153,2,370,4,6,371,1634]
l2=[]
for i in l1 :  # 1
    count =0    
    for  j in range(1,i+1):  #  2, 2
        if i % j ==0:   # 1 % 1 == 0
            count +=1   # 1
    if count ==2 :
        l2.append(i)
print(l2)
