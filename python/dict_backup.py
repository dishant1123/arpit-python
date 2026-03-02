#dict : mutable  :  key  value  pair  

"""
d1 ={"phy"  :85  , "che" :77} 

# phy  key  85 vlaue    che key 77 value
print(d1)
print(type(d1))

"""
"""
d2 ={89 : 78 , "vyom" :21}
print(d2)
print(type(d2))
"""

# add :

"""
d1 ={"phy"  :85  , "che" :77} 

d1["maths"] = 90
print(d1)
"""

# built in function  : len min max sorted  sum 
"""
d1 ={"phy"  :85  , "che" :77} 
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))

"""

# method : 
d1 ={"phy"  :85  , "che" :77, "maths":88, "com" :99} 

"""d1.clear()
print(d1)
"""
"""d2 =d1.copy()
print(d2)
"""
l1 = ["ankit", "purvesh"]
# {"ankit":100 , "purvesh" : 100}

"""
d2 =dict.fromkeys(l1,100)
print(d2)
d2["ankit"]=200
print(d2)
"""
"""print(d1.get("phy"))
print(d1.keys())
print(d1.values())
print(d1.items())
"""

"""d2={"ankit":100 , "purvesh" : 100}

d1.update(d2)
print(d1)
"""

"""d1.pop("phy")
print(d1)"""

"""d1.popitem()
print(d1)
"""
"""d1.setdefault("ss",100)
print(d1)
"""
"""
1. Ask user to give name and marks of 10 different students. Store them in dictionary.

user  = 3 
name  marks
ankit  100  purvesh 45 vyom 90  
{"ankit" : 100 , "purvesh" : 45 , "vyom" : 90}

2. Sort the above dictionary in ascending order of Marks.

"""