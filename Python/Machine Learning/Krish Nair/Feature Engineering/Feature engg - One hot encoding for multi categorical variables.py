# todo: Importing Library
import pandas as pd
import numpy as np

# todo: let's load the mercedes benz dataset for demonstration only the categorical variables
data = pd.read_csv('mercedez benz - train.csv', usecols=['X1', 'X2', 'X3', 'X4', 'X5', 'X6'])
data.head()

# todo: let's have a look at how many labels each variable has
for col in data.columns:
    print(col, ':', len(data[col].unique()), 'labels')

# todo: let's examine how many columns we will obtain after one hot encoding these variables
print(pd.get_dummies(data, drop_first=True).shape)

# we can see that from just 6 initial categorical columns, we end up with 117 new columns hence
# we can perform one hot encoding only for 10 most frequently used variables and take 0 for less frequent variables.

# todo: lets find the top 10 most frequent categories for the column X2
data.X2.value_counts().sort_values(ascending=False).head(20)

# todo: lets make a list with the most frequent categories of the variable
top_10 = [x for x in data.X2.value_counts().sort_values(ascending=False).head(10).index]
print(top_10)

# todo: and how we make the 1, 0 binary variables
for label in top_10:
    data[label] = np.where(data['X2'] == label, 1, 0)
data[['X2'] + top_10].head(40)

# todo: get whole set of dummy varibles, for all the categorical variables
def one_hot_top_x(df, variable, top_x_labels):
    # function to create the dummy variables for the most frequent labels
    # we can vary the number of most frequent labels that we encode
    for label in top_x_labels:
        df[variable + '_' + label] = np.where(data[variable] == label, 1, 0)

# todo: read the data again
data = pd.read_csv('mercedez benz - train.csv', usecols=['X1', 'X2', 'X3', 'X4', 'X5', 'X6'])

# todo: encode X2 into the 10 most frequent categories
one_hot_top_x(data, 'X2', top_10)
data.head()

# todo: find the 10 most frequent categories for X1
top_10 = [x for x in data.X1.value_counts().sort_values(ascending=False).head(10).index]

# todo: now create the 10 most frequent dummy variables for X1
one_hot_top_x(data, 'X1', top_10)
data.head()

# todo: For other columns do same one hot encoding

# One hot encoding of top variables
# Advantages
# 1) Straight forward to implement
# 2) Does not require hrs of variable exploration
# 3) Does not require massively the feature space (number of columns in the dataset)

# Disadvantage
# 1) Does not add any information that may make the variable more predictive
# 2) Does not keep the information of the ignored labels
