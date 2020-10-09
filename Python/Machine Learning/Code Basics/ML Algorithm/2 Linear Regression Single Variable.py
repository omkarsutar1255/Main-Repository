# todo: Import libraries
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# todo: Load DataSet
df = pd.read_csv('homeprices.csv')
print(df)

# todo: plotting graph on train dataset
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area, df.price, color='red', marker='+')

# todo: creating separate column of only area and price
new_df = df.drop('price', axis='columns')
print(new_df)
price = df.price
print(price)

# todo: Create linear regression object
reg = linear_model.LinearRegression()
reg.fit(new_df, price)

# todo: Predict price of a home with area = 3300 sq ft
reg.predict([[3300]])

# todo: Y = m * X + b (m is coefficient and b is intercept)
print(reg.coef_)
print(reg.intercept_)
print(3300 * 135.78767123 + 180616.43835616432)

# todo: Predict price of a home with area = 5000 sqr ft
reg.predict([[5000]])

# todo: Generate CSV file with list of home price predictions
area_df = pd.read_csv("areas.csv")
area_df.head(3)

# todo: Prediction on test dataset
p = reg.predict(area_df)
print(p)
area_df['prices'] = p
print(area_df)

# todo: Saving Prediction in CSV File
area_df.to_csv("prediction.csv")
