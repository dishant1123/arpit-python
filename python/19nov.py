import  numpy as np  

"""a=np.array([1,2,3,4,5,6])
print(a)

b=np.arange(1,21,2)
print(b)

c=np.arange(1,21,2).reshape(2,5)
print(c)

d=np.zeros((2,3),dtype= int)
print(d)

f=np.ones((2,3),dtype=int)
print(f)

g=np.full((2,4),fill_value=100)
print(g)

h=np.full_like(a,fill_value=10).reshape(3,2)
print(h)
"""

a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]]
)
# print(a)
# print(a.shape)

# print(a[0])
# print(a[1:4])

b=np.arange(1,31).reshape(6,5)
print(b)


