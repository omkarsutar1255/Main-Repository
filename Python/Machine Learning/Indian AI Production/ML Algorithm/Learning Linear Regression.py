# todo: Import library
import pandas as pd

# todo: Load dataset
df = pd.read_csv("Bengaluru_House_Data.csv")
print(df.head())
# df = df.drop('availability', axis=1)
print(df.info())
# print(df['location'].value_counts())
l1 = ['area_type', 'availability', 'location', 'size', 'society', 'total_sqft']
for i in l1:
    j = df[i].nunique()
    if j > 1000:
        df = df.drop(i, axis=1)

print(df.info())
# print(df['location'].nunique())

print(df.isnull().sum())
df['size'] = df['size'].fillna(df['size'].mode()[0])
df['bath'] = df['bath'].fillna(df['bath'].mean())
df['balcony'] = df['balcony'].fillna(df['balcony'].mean())
print(df.isnull().sum())

df = pd.get_dummies(df, drop_first=True)
print(df.shape)
print(df.columns)

# todo: splitting features and label column
X = df.drop('price', axis=1)
y = df['price']
print("shape of x = ", X.shape)
print("shape of y = ", y.shape)

# todo: splitting into test and train dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print("X_train shape = ", X_train.shape)
print("X_test shape = ", X_test.shape)
print("y_train shape = ", y_train.shape)
print("y_test shape = ", y_test.shape)
print("null value in y_test = ", y_test.isnull().sum())

# todo: Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)    # learned the parameter for scaling in both set
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# todo: Linear regression ML model training
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
print(lr.intercept_)

# todo: predict the value of Home and Test
# print(lr.predict([X_test[0, :]]))   # prediction of first house
# tf = pd.DataFrame()
# tf['predict'] = lr.predict(X_test)
# tf['y_test'] = y_test.to_numpy()      # converted pandas series into numpy
# print(tf.head(20))

# todo: Evaluation of model
# print(type(X_test))
# print(type(y_test))
y_pred = lr.predict(X_test)
# print(type(y_train_pred))
# print(lr.score(X_test, y_test))
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))
