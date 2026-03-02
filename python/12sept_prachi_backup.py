
# for loop  : 
"""
1.for 
2.while  
3.while True
"""
"""
syntax : 

for  variable  in range(start , end ,step):
    print()
"""
# 1-100 :
"""
for i in range(1,101):
    print(i,end= " ")

"""
# 100-1 : 
"""
for i in range(100,1,-1):
    print(i,end= " ")
"""

# start , stop  : 

"""start =int(input("enter start : "))
stop =int(input("enter stop : "))

for i in range(start,stop+1,2):
    print(i,end=" ")
"""

# prime , perfect , amg , twin  pelindorme , reverse , : 

# prime  : 2 factors : 
# perfect :  6 factors :1,2,3,6 ==>sum .= 1+2+3 =6  28 

"""n=int(input("enter the  number  :" ))
count =0 

for i in range(1,n+1):
    if n % i ==0 :
        count +=1 
if count ==2 :
    print(n,"is prime")
"""

# amg : 
# len min  max sorted 

"""n=int(input("enter the  number  :" ))
digits = len(str(n))   # 1634 
print(digits)   #4 
sum =0
temp =n 
for i in range(digits):  # 3,4 
    r=  temp  % 10     # r= 1 %10 =1    
    sum =sum + pow(r,digits)  # sum =1634 
    temp =  temp // 10        # temp =1 //10 =0  
if sum == n : 
    print(n,"is amg")

"""

# adv list : 

# l1=[[1,2,3],[4,5,6],[7,8,9]]  # 2d array : 
"""print(l1)

for i in l1 :
    print(i)
"""
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

r  c
(0,0)1  (0,1)2  (0,2)3 
(1,0)4  (1,1)5  (1,2)6
(2,0)7  (2,1)8  (2,2)9
"""
"""l1=[[1,2,3,56,78],
    [4,5,6,90,11],
    [7,8,9,78,67],
    [10,22,33,44,55]]  # 2d array : 
"""
"""print(l1[0])
print(l1[2])

print(l1[0][2:4])  # 0 row  2 index  to  4 index 
print(l1[2][1:3])
print(l1[3][1 : 4 :2])# 1 start  4 end   2 step size 
print(l1[2][  :   :2])#  start   end   2 step size 
print(l1[2][  :   :-2])#  start   end   2 step size 
print(l1[3][  :   :-1])#  start   end   1step size 
"""

# transpose : 

l1=[[1,2,3],
    [4,5,6],
    [7,8,9]]  
print(len(l1[0]))
"""
output  : 
[1 4 7]
[2 5 8]
[3 6 9]

"""
"""
for i in range(len(l1[0])) :# 1 ,3 
    l2=[] 
    for j in range(len(l1)):  # 1,3
        l2.append(l1[j][i])   # l1[1][1]
    print(l2)                  # 1 4  7
                               # 2 5 
"""

"""
l1=[[1,2,3],
    [4,5,6],
    [7,8,9]]  

output  : 

1 row  sum = 6 
2 row sum = 15 
3 row sum = 24 
1 col sum =12 
2 col sum =15
3 col sum =18
"""
