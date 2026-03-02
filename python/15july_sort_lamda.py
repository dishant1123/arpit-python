"""
1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

hint  : 
0 index : ('English', 88)  ==> eng==>0   80 ==>1 
1 index : ('Science', 90)  ==> sci==>0   90 ==>1
2 index : ('Maths', 97) ==> maths==>0   97 ==>1
3 index : ('Social sciences', 82) ==> soc==>0   82 ==>1

"""
"""
l1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a= sorted(l1,key=lambda x : x[1])
print(a)
"""