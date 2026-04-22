# linear regression  : 
"""
uses one  independent variable X to  predict one dependent variable Y. 

y = mx+c

y= dependent variable (output)
x= independent variable (input)
m= slope
c= intercept
"""
"""from sklearn.linear_model import LinearRegression
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns
"""
"""# one  area  and  price
x=np.array([[1000],[1500],[2000],[2500]])  # area  ==> 3000 
y=np.array([150000,200000,250000,300000])  # price  ==> ? 

model = LinearRegression()
model.fit(x,y)

# predict  : 
print("predict price : ",model.predict([[3000]]))
"""
# multiple linear regression  :  use more than one independent variable. 

"""x = np.array([
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
"""

# polynomial regression 
"""
it is extention of linear regression where the relationship  between input  x and  ouput y  is non linear but model still use to  linear regression.

linear  regression  : y = mx +c 

poly : y= b0  + b1x + b2x^2  + b3x^3 .....

use :
1.data shown a curve pattern. 
2. linear regression  poor accuracy.

x     y
1     1
2     4
3     9
4     16
5     25

y = x^2 
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([1,4,9,16,25])

poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly,y)

y_pred = model.predict(x_poly)

plt.plot(x,y,'o',label='data')
plt.scatter(x,y_pred,color='red',label='prediction')
plt.plot(x,x*x,'--',label='line')
plt.legend()
plt.show()




