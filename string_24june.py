#string  : immutable sequence of characters == > no changes in string  

"""
s1 = "my name is arpit."

print(s1)
print(type(s1))

"""

# built-in function  :  len  min max sorted 


"""s1 = "my name is arpit."
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))

"""
# slicing  : [start  ,stop  , step ]  

"""
s1 = "my name is arpit."

# pos index :  l to r    : 0 
# neg index :  r  to l   : -1 

print(s1[2])
print(s1[1 : 5])
print(s1[ : 5])
print(s1[ 1: ])
print(s1[2 : 6 : 2]) # start  2   end 6  step : 2 
print(s1[1 : 10 : 3]) # start  2   end 6  step : 2 
print(s1[ : : -2])
print(s1[ : : -1])
"""
"""
task  : 1 
input  :  dishant dipakkumar shah 
output  : d.d.shah

task  : 2 
ask user to enter the two string  and inter change the  first three letter of the string. 

input  a :color 
input  b :full 

output  a :fulor
output  b :coll
"""
s1 = "My Name is arpit arpit."

"""print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.title())
print(s1.casefold())
"""

# print(s1.replace("arpit","prakashbhai"))
# print(s1.replace("arpit","prakashbhai",1))

"""
task  : 1 

input  : "restart"
output  : resta@t

task  : 2  
input  : my name is arpit prakashbhai jain. 
output : my_name is arpit prakashbhai_jain.
"""

"""
s1 =  "restart"
s2 =s1[0]
# print(s1)

modify_string = s2 + s1[1 :].replace(s2,"@")
print(modify_string)

"""

"""s1 = "my name is arpit prakashbhai jain."

modify_string = s1.replace(" ","_",1) [: : -1].replace(" ","_",1)[: : -1]
print(modify_string)
"""

