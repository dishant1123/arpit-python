# dict  == >  mutable changes in dict   ==> key  value pair  

"""
d1 ={"arpit":20 , "vyom":21 , "anuj":22}

# arpit  == key  ==value  20    vyom  ==> key   21 value  
print(d1)
print(type(d1))

d2={20 : 21 , 56 : "arpit" }
print(d2)
print(type(d2))
"""

# dict is  mutable 

"""
d1 ={"arpit":20 , "vyom":21 , "anuj":22}
print(d1)

d1["dishant"]=23
print(d1)

"""

# dict  : built in function   :  len  min max sorted  

"""
d1 ={"arpit":45 , "vyom":21 , "anuj":22}

print(len(d1)) 
print(min(d1))  # anuj 
print(max(d1))  # vyom 
print(sorted(d1))#   
"""

# method  : 

d1 ={"harsh":45 , "vyom":21 , "anuj":22,"sapan" :80}

# d1.clear()
# print(d1)

# d2=d1.copy()
# print(d2)

# print(d1.get("anuj"))

"""print(d1.keys())
print(d1.values())
print(d1.items())
"""


"""
l1 = ["ram","sita"]
# {"ram" :100 , "sita" : 100}
d2 = dict.fromkeys(l1,100)
print(d2)
"""
# d2["sita"]=200
# print(d2)


"""d1.update(d2)
print(d1)
"""

"""d1.pop("harsh")
print(d1)
"""

"""
d1.popitem()
print(d1)
"""

"""
task  : 1 ask user to enter the  3  student name  and marks and store  in to dict.
ram  200  ravan  800  sita 400 

d1 ={"ram" : 200 , "ravan" : 800 , "sita" : 400}

l1= sorted(d1.values())  # [200 , 400 ,800]
d2 ={}
for  i in l1 : [200 , 400 , 800 ]
    for j, k in d1.items():{"ram" : 200 , "ravan" : 800 , "sita" : 400}

task  : 2 above   dict sort of name  dec to asc    

{"ram" :200 ,"sita" : 400 ,"ravan" : 800  }

task  : 3 ask user to enter the  string  and  count  the  words in string  and store  in to dict.

input  : "mississippi"
output  : {"m" : 1 , "i" : 4 , "s" : 4 , "p" : 2 }
"""

"""
s = input("enter the string  : ")
d1={}
for i in s : 
    d1[i] =s.count(i)
print(d1)
"""
"""s = input("enter the string  : ") # mississippi
d1={}
for i in s :  # mississippi
    if i in  d1:   #  s in d1  
        d1[i] += 1 # s 4 i 4 
    else :
        d1[i] = 1  # m  1  i 1  s 1 
print(d1)
"""
print(len("helloworld"))

"""s = 1,5,6
print(s)
print(type(s))

s1={"apple"}
print(s1)
print(type(s1))

s2 =dict("apple")
print(s2)
print(type(s2))
"""

"""
s1 = ("saloni")
print(s1)
print(type(s1))
"""

