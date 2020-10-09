# todo: Categorical Variables and One Hot Encoding

# todo: Importing Libraries
import pandas as pd

# todo: Load DataSet
df = pd.read_csv("homeprices.csv")
print(df)

# todo: Using pandas to create dummy variables
dummies = pd.get_dummies(df.town)
print(dummies)

# todo: concatenate dummies with data
merged = pd.concat([df, dummies], axis='columns')
print(merged)

# todo: dropping original dummy column
final = merged.drop(['town'], axis='columns')
print(final)

# todo: Dummy Variable Trap
# When you can derive one variable from other variables, they are known to be multi-colinear. Here
# if you know values of california and georgia then you can easily infer value of new jersey state, i.e. 
# california=0 and georgia=0. There for these state variables are called to be multi-colinear. In this
# situation linear regression won't work as expected. Hence you need to drop one column. 

# NOTE: sklearn library takes care of dummy variable trap hence even if you don't drop one of the
#     state columns it is going to work, however we should make a habit of taking care of dummy variable
#     trap ourselves just in case library that you are using is not handling this for you

# todo: Dropping one of dummy variable column for not happen dummy variable trap
final = final.drop(['west windsor'], axis='columns')
print(final)

# todo: Splitting Features and Label DataSet
X = final.drop('price', axis='columns')
y = final.price

# todo: Creating model and Prediction and score
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
model.predict(X)  # 2600 sqr ft home in new jersey
model.score(X, y)
model.predict([[3400, 0, 0]])  # 3400 sqr ft home in west windsor
model.predict([[2800, 0, 1]])  # 2800 sqr ft home in robbinsville

# todo: Using SkLearn OneHotEncoder
# todo: First step is to use label encoder to convert town names into numbers
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = df
dfle.town = le.fit_transform(dfle.town)
print(dfle)   # transform categorical values into 0, 1, 2, 3...

# todo: Splitting into Features and Label
X = dfle[['town', 'area']].values
print(X)
y = dfle.price.values
print(y)

# todo: Now use one hot encoder to create dummy variables for each of the town
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('town', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)            # converting 0, 1, 2, 3,.. into one hot encoding
print(X)
X = X[:, 1:]         # dropping first column of one hot encoding
print(X)
model.fit(X, y)          # training model
model.predict([[0, 1, 3400]])  # 3400 sqr ft home in west windsor
model.predict([[1, 0, 2800]])  # 2800 sqr ft home in robbinsville
