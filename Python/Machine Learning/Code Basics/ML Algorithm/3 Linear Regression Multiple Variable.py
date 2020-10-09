# todo: Machine Learning With Python: Linear Regression Multiple Variables

# todo: Import Libraries
import pandas as pd
import numpy as np
from sklearn import linear_model

# todo: Load DataSet
df = pd.read_csv('homeprices.csv')
print(df)

# todo: Data PreProcessing: Fill NA values with median value of a column
df.bedrooms.median()
df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
print(df)

# todo: create Linear Regression Model
reg = linear_model.LinearRegression()
reg.fit(df.drop('price', axis='columns'), df.price)
print(reg.coef_)
print(reg.intercept_)

# todo: Find price of home with 3000 sqr ft area, 3 bedrooms, 40 year old
print(reg.predict([[3000, 3, 40]]))
print(112.06244194 * 3000 + 23388.88007794 * 3 + -3231.71790863 * 40 + 221323.00186540384)

# todo: Find price of home with 2500 sqr ft area, 4 bedrooms,  5 year old
print(reg.predict([[2500, 4, 5]]))
