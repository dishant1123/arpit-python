"""
while  loop  :  exit control  loop  
for  : entry control loop 
"""

"""i=1 
while i <=10 :
    print(i)
    i+=1
"""

# break continue  pass 

"""
i =1 
while i<=10: 
    print(i)
    i+=1
    if i==5:
        break
"""

# continue : 
"""i =1 
while i<=10: 
    print(i)
    if i==5:
        continue
    i+=1
    
"""
# contunie:    itration  skip  contunie  for  next iteration. 

"""
for i in range(1,10):
    if i==5:
        continue
    print(i)
"""

# pass : 

"""i=1
while i<=10:
    if i==5:
        pass
    print(i)
    i+=1
"""    

# while true  : 
"""
i=1 
while True:
    print(i)
    i+=1
    if i==10:
        break
"""    
# strong number  : 
"""
145  == strong number  

1 ! = 1 
4!  = 4*3*2*1 = 24 
5! =5*4*3*2*1 = 120 

sum = 1+120+24 = 145  strong number  
"""
l1 =[1,2,3,145,456,789]
l2=[]
# strong number  : 145 
for i in l1:
    temp = i   #   temp = 145
    while temp > 0:  # 145 > 0 
        r = temp %  10
        fact=1 
        sum =0 
        j= 1 
        while j<=r:
            fact = fact * j
            j+=1
        sum = sum + fact   # sum = 0 + 1 = 1 
        temp = temp // 10  # 145 // 10 = 14
    if sum ==i:  # 1 == 1 
        l2.append(i)
print(l2)
