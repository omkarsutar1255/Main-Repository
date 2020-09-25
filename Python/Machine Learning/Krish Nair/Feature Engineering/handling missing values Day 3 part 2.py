# todo: Handle Categorical Features
# todo: One Hot Encoding

# todo: import library
import pandas as pd
import numpy as np

# todo: load dataset
df = pd.read_csv('titanic.csv', usecols=['Sex'])
df.head()

# todo: creating dummy variable for categorical variable
pd.get_dummies(df, drop_first=True).head()

# todo: loading dataset
df = pd.read_csv('titanic.csv', usecols=['Embarked'])
df['Embarked'].unique()
df.dropna(inplace=True)
pd.get_dummies(df, drop_first=True).head()

# todo: Onehotencoding with many categories in a feature
df = pd.read_csv('mercedes.csv', usecols=["X0", "X1", "X2", "X3", "X4", "X5", "X6"])
df.head()

# todo: show how many unique values every column have
for i in df.columns:
    print(len(df[i].unique()))

# todo: show top 10 most frequent categories in column
df.X1.value_counts().sort_values(ascending=False).head(10)

# todo: getting most frequent values without their occurrence number
lst_10 = df.X1.value_counts().sort_values(ascending=False).head(10).index
lst_10 = list(lst_10)  # convert it into a list
print(lst_10)

# todo: creating column of one hot encoding only for top most frequent categories
for categories in lst_10:
    df[categories] = np.where(df['X1'] == categories, 1, 0)

# todo: adding X1 feature to list of most frequent categories
lst_10.append('X1')
print(df[lst_10])  # represent one hot encoding
