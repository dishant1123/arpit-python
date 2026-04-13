"""
python  : object  oriented programming  

1. data cleaning   
2. data analysis  
3. hacking  
4. GUI  : graphical user interface 
5. web scraping

# extention  : .py ==> python   , jpg/png ==>picture , xlsx ==> excel  

# run : VS code , google colab , jupyter notebook , spyder

#include<stdio.h>
#include<conio.h>
void main()
{
    printf("hello"); 
    return 0 ;
}
"""
"""
print("hello world\n")
print("my name is ram.")
"""
# comment : 
"""
1 .single line  comment  : # (hash)  shor cut : ctrl + / 
2. multi lien comment : """ """ or ''' ''' 
"""

# print("hello world")
"""
print("my name is ram.")
print("my name is sita. ")
print("age is  23")
"""

# data type  : 
"""
1. int  : number   ==> no  limit 
2. float : decimal number
3. string / char : name  , character
4. bool : True or False
5. complex number  : i or j  
    ex : 23 + 8j    
        2 part  : 1. real part  :23  2. imaginary part : 8j
"""
"""
variable  declaration rules : 

1. variable  not start with  : special character , number , between special character
2. underscore  , ending number  ==> it is  valid   
"""
"""
a=10 
print(a)
print("a=",a)
print(type(a))

b=12345678123456783456783456784356784567
print(b)
print("b=",b)
print(type(b))

c= 12.45
print(c)
print("c=",c)
print(type(c))

d= 1234567233.45677889999999992344
print(d)
print("d=",d)
print(type(d))

e="yagna"
print(e)
print("e=",e)
print(type(e))

f=True
print(f)
print("f=",f)
print(type(f))

g=23+7j 
print(g)
print("g=",g)
print(type(g))
h=12 +8j 
print(g+h)
"""

# user input number  : 
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

a=float(input("enter the  number  : "))
b=float(input("enter the  number  : "))

print("a=",a)
print("b=",b)
print("sum of a and b=",a+b)

"""

# user input string  :

"""
a=input("enter the string : ")
b=str(input("enter the string : "))
print("a=",a)
print("b=",b)
print(a+b)
"""

# task :1 ask user to enter the  5 int type  number  and print  avg of them . 
# task :2 ask user to enter the  string and concate . 
"""
input  a = "ram"
input  b = "sita"
output  :ram sita  
"""

# operator  : 

"""
1. airthematic : + - * / %  // 
    % ==> modulo  ==> give  reminder
    // ==> floor division  ==> give  integer
    
2. relational : == != > < >= <=
3. logic : and ,or ,not
4. assignment : = += -= *= /= //= %=
"""

# print(10 % 2)
# print(13 % 3)
# print(25 % 4)
# print(10 /3 )
# print(10//3)  # // ==> floor division  ==> give  integer
# print(12 // 5)

# a=106 
# b=106
# print(a!=b)

# a=9
# b=89 

# print(a>b and a!=b )
# print(a>b or a!=b )

# a=12 
# b=45 

# a= a+b
# a+=b   
# print(a)


# task  :3  ask user  to enter  the  2  number : add , sub , mul , div , mod , floor div  ,  print  the  result  .

# conditional statement  : 
"""
syntax :

if condition :
    statement
else: 
    statement
"""
# ex :1 
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b:
    print("a is greater than b")
else :
    print("b is greater than a")

"""

# ex :2 leap year  : every 4 year 

"""year =int(input("enter the  year  : "))

if year % 4 ==0 : 
    print("leap year")
else : 
    print("not leap year")
"""

# ex :3 ladder if : 
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b:
    print("a is greater than b")
elif b >a:
    print("b is greater than a")
else :
    print("same")
"""

# ladder if  :

a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b :   # a=10  b=90  c=900 
    if a>c :
        print("a is  big")
    else : 
        print("c is  big")

elif b>a : 
    if b>c :
        print("b is  big")
    else :
        print("c is  big")
else : 
    print("same")
        