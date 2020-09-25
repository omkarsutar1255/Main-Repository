# todo: Importing Library
import pandas as pd
import numpy as np

# todo: Loading dataset
df = pd.read_csv('mercedez benz - train.csv', usecols=['X1', 'X2'])

# todo: analysis dataset
df.head()
df.shape()

# todo: One hot encoding
print(pd.get_dummies(df).shape)
len(df['X1'].unique())
len(df['X2'].unique())

# todo: checking which column has how many labels
for col in df.columns[0:]:
    print(col, ':', len(df[col].unique()), 'labels')

# lets obtain the counts for each one of the lables in variables X2
# lets capture this in a dictionary that we can use to remap the labels
df.X2.value_counts().to_dict()

# and now lets replace each label in X2 by its count
# first we make a dictionary that we maps each label to the counts
df_frequency_map = df.X2.value_counts().to_dict()

df.X2.head()

# and now we replace X2 label in the dataset df
df.X2 = df.X2.map(df_frequency_map)
df.head()

# Advantages
# 1)It is very simple to implement
# 2)Does not increase the feature dimensional space

# Disadvantage
# 1)If some of the labels have the same count, then they will be replaced with the same count and
# they will lose same valuable information.
# 2) Adds somewhat arbitrary numbers and therefore weights to the different labels,
# that may not be related to their predictive power.
