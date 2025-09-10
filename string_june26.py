s1 = "my name is yash  parikh." 

"""print(s1.center(89,"-"))
print(s1.ljust(100,"-"))
print(s1.rjust(100,"-"))

"""
"""print(s1.removeprefix("my"))
print(s1.removesuffix("parikh."))
"""

s2="12arpit"

# print(s2.isalpha())
# print(s2.isdigit())

# print(s2.isalnum())

"""s3=["i" ,"love","india."]
# i love india 
print(" ".join(s3))
print(str(s3))


print(s1.count("i",8 , 20))
"""
"""
task : 12 
Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']

Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
"""
l1 =[(('cat', 'dog', 'fear', 'center'))]
l2=[]
for i  in  l1:  # cat 
    n =input("enter the word : ") # ca
    for j in i :  #  j =cat
        if n in j:  # 
            l2.append(j)
print(l2)


"""s3 ="my name is yash  parikh."
print(s3.startswith("my"))
print(s3.endswith("parikh."))"""

"""
Write a Python program to test a list of one hundred integers between 0 and 999, 
which all differ by ten from one another. Return True otherwise False.
Input:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
output  :  true
"""

l1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
i=0 
result = True 

while i < len(l1) -1 :     #  0 < 13  -1  
    if  l1[i+1] - l1[i] != 10:   # l1 [1] - l1[0] != 10 
        result = False      
        break
    i += 1
print(result) 

