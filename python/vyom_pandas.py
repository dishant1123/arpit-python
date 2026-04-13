import pandas as pd
import numpy as np


"""a= pd.Series([1,23,45,67,89,90])
print(a)
print(a.shape)
print(a.info())
print(a.describe())
"""
"""
a = pd.DataFrame({
    "name": ["John", None, "Jack", "Jill"],
    "age": [20, 25, 22, None],
    "salary": [5000, 4000, 3000, 2500]
})
# print(a)
# print(a.info())
# print(a.describe())
print(a.dropna(how="all"))"""

"""import pandas as pd
import numpy as np
df=pd.DataFrame([[0,1.0,2.0,np.nan,5],[2.0,0,1.0,5.0,np.nan],[5.0,0,1.0,np.nan,5.0]])
# print(df.dropna())
print(df.loc[1,3])
print(df)
"""

"""df=pd.DataFrame([[0,1,2,np.nan,5],[2,0,1,5,np.nan],[5,0,1,np.nan,5],[2,0,1,np.nan,np.nan]])
df=df.drop_duplicates(subset=[1,2])
df=df.drop_duplicates(subset=[4])
"""
# df =df.dropna(thresh=2,axis=1)
# print(df)

"""print(df.shape)
print(df.mean())
"""
"""
   0  1  2    3    4
0  0  1  2  NaN  5.0
1  2  0  1  5.0  NaN
2  5  0  1  NaN  5.0
3  2  0  1  NaN  NaN
"""

# df=pd.DataFrame([[1,2,3,4,5],[2,1,3,4,5],[np.nan,np.nan,np.nan,np.nan,np.nan]])
# print(df)
# df.dropna(thresh=2,axis=1,inplace=True)   
# print(df.shape[1])
# df.drop(1,inplace=True)
# df=df.dropna()
# print(df.shape[0])
# print(df)

"""data = {
    "Student": ["A","B","C","D","E"],
    "Math": [78, 90, 67, 88, 90],
    "Science": [85, 92, 70, 88, 85]
}
df = pd.DataFrame(data)
print(df)"""
# print(df.sort_values(by=['Math']))
# print(df.sort_values(by=['Math'],ascending=False))
# print(df.sort_values(by=['Math','Science'], ascending=[False,True]))


# result = df.sort_values(by=["Math","Science"], ascending=[False,True])
# print(result.head(1)["Student"].values[0])


# df = pd.DataFrame({
#     "B":[1,2],
#     "A":[3,4],
#     "C":[5,6]
# })
# print(df)
# print(df.sort_index())
# print(df.sort_index(axis =1))
# print(df.sort_index(axis =0,ascending=False))

# df2 = df.sort_index(axis=1)
# print(df2.columns[0])

# df1 = pd.DataFrame({"A":[1,2]})
# df2 = pd.DataFrame({"B":[3,4]})
# result = pd.concat([df1, df2],ignore_index=False)
# print(result)
# print(result.index[3])

"""import pandas as pd
df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A","B","C"]
})
df2 = pd.DataFrame({
    "ID":[2,3,4],
    "Marks":[80,90,70]
})

result = pd.merge(df1, df2, how="inner", on="ID")
print(result)
print(len(result))
"""

"""df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A","B","C"]
})
df2 = pd.DataFrame({
    "ID":[2],
    "Marks":[80]
})
result = pd.merge(df1, df2, how="left", on="ID")
print(result)
print(result["Marks"].isnull().sum())
"""

import pandas as pd
"""df = pd.DataFrame({
    "Team":["X","Y","X","Y","X"],
    "Runs":[50,60,70,80,90]
})
result = df.groupby("Team")['Runs'].mean()
print(result)
"""

"""df = pd.DataFrame({
    "Category":["A","A","B","B"],
    "Value":[10,20,30,40]
})
result = df.groupby("Category").agg({"Value":["sum","max"]})
print(result.loc["B",("Value","sum")])
"""

"""df = pd.DataFrame({
    "Team":["X","X","Y","Y"],
    "Score":[10,20,30,40]
})
print(df)
result = df.groupby("Team").nth(1)
print(result.loc["X"])
"""


data = {
    "name": ["William", "Emma", "Sofia", "Markus", "Edward",
             "Thomas", "Ethan", np.nan, "Arun", "Anika", "Paulo"],
    "region": [np.nan, "North", "East", np.nan, "West",
               "West", "South", np.nan, "West", "East", "South"],
    "sales": [50000, 52000, np.nan, np.nan, 42000,
              72000, 49000, np.nan, 67000, 65000, 67000],
    "expenses": [42000, 43000, np.nan, np.nan, 38000,
                 39000, 42000, np.nan, 39000, 50000, 45000]
}

df = pd.DataFrame(data)
print(df)
def remove_outliers_iqr(df, columns):
    df_clean = df.copy()
    
    for col in columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    
    return df_clean
numeric_cols = df.select_dtypes(include=np.number).columns
df_clean = remove_outliers_iqr(df, numeric_cols)

print(df_clean)
"""
import pandas as pd

df = pd.DataFrame({
 'Marks': [50, 55, 60, 65, 70, 75, 200] # 200 is an outlier
})
print("Original Data:\n", df, "\n")

Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
# Step 2: Calculate IQR
IQR = Q3 - Q1
# Step 3: Define bounds
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print("Lower Bound:", lower)
print("Upper Bound:", upper, "\n")

outliers = df[(df['Marks'] < lower) | (df['Marks'] > upper)]
print("Outliers:\n", outliers, "\n")

df_clean = df[(df['Marks'] >= lower) & (df['Marks'] <= upper)]
print("Data after removing outliers:\n", df_clean)"""

import pandas as pd

df = pd.DataFrame({
    "Student":["A","B","C","D"],
    "Math":[70,45,90,60],
    "Science":[75,40,85,55]
})

df['avg'] =df.apply(lambda x :(x['Math']+x['Science'])/2,axis=1) 
print(df)

def average(df):
    if df['avg'] >80 :
        return "Distinction"
    elif df['avg'] >60 :
        return "Frist"
    else :
        return "Second"
    
df['grade'] =df.apply(average,axis=1)
print(df)
