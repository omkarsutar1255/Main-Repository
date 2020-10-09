# todo: Save And Load Trained Model

# todo: Import Libraries
import pandas as pd
import numpy as np
from sklearn import linear_model

# todo: Load DataSet
df = pd.read_csv("homeprices.csv")
df.head()

# todo: Creating Linear Regression Model
model = linear_model.LinearRegression()
model.fit(df[['area']], df.price)
print(model.coef_)
print(model.intercept_)

# todo: Model Prediction
model.predict([[5000]])

# todo: Save Model To a File Using Python Pickle
import pickle
with open('model_pickle', 'wb') as file:
    pickle.dump(model, file)

# todo: Load Saved Model
with open('model_pickle', 'rb') as file:
    mp = pickle.load(file)
print(mp.coef_)
print(mp.intercept_)
print(mp.predict([[5000]]))

# todo: Save Trained Model Using joblib
import joblib
joblib.dump(model, 'model_joblib')

# todo: Load Saved Model
mj = joblib.load('model_joblib')
print(mj.coef_)
print(mj.intercept_)
print(mj.predict([[5000]]))
