# linear regression  : 
"""
uses one  independent variable X to  predict one dependent variable Y. 

y = mx+c

y= dependent variable (output)
x= independent variable (input)
m= slope
c= intercept
"""
from sklearn.linear_model import LinearRegression
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns

"""# one  area  and  price
x=np.array([[1000],[1500],[2000],[2500]])  # area  ==> 3000 
y=np.array([150000,200000,250000,300000])  # price  ==> ? 

model = LinearRegression()
model.fit(x,y)

# predict  : 
print("predict price : ",model.predict([[3000]]))
"""
# multiple linear regression  :  use more than one independent variable. 

x = np.array([
    [1000,2],
    [1500,3], 
    [2000,3],
    [2500,4]   
])

y=np.array([150000,200000,2600000,3200000])

model = LinearRegression()
model.fit(x,y)

# predict : 
# print("predict  price : ",model.predict([[3000,4]]))

area = x[:,0]
bedroom = x[:,1]

plt.scatter(area,y)
plt.xlabel("area")
plt.ylabel("price")
plt.title("Price vs Area")
plt.show()

