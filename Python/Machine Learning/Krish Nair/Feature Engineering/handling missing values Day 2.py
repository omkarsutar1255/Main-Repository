# todo: 1. Random Sample Imputation

# Aim: Random sample imputation consists of taking random observation from the dataset and
# we use this observation to replace the nan values

# todo: When should it be used?
# It assumes that the data are missing completely at random(MCAR)

# todo: import library
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# todo: loading dataset
df = pd.read_csv('titanic.csv', usecols=['Age', 'Fare', 'Survived'])

# todo: analysis dataset
df.head()
df.isnull().sum()
df.isnull().mean()
df['Age'].isnull().sum()

# todo: replacing null values of column with random values of that column
df['Age'].dropna().sample(df['Age'].isnull().sum(), random_state=0)

# todo: index of null values in age column
print(df[df['Age'].isnull()].index)

# todo: function that gives new column with filled median values at null values
def impute_nan(df, variable, median):
    df[variable + "_median"] = df[variable].fillna(median)
    df[variable + "_random"] = df[variable]

    # It will have the random sample to fill the na
    random_sample = df[variable].dropna().sample(df[variable].isnull().sum(), random_state=0)

    # pandas need to have same index in order to merge the dataset
    random_sample.index = df[df[variable].isnull()].index
    df.loc[df[variable].isnull(), variable + '_random'] = random_sample

# todo: checking median value of age column of dataset
median = df.Age.median()
print(median)

# todo: calling function that gives two column with median values and random sample values
impute_nan(df, "Age", median)
df.head()

# todo: checking distribution of dataset in graphical manner
fig = plt.figure()
ax = fig.add_subplot(111)
df['Age'].plot(kind='kde', ax=ax)
df.Age_median.plot(kind='kde', ax=ax, color='red')
df.Age_random.plot(kind='kde', ax=ax, color='green')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')

# todo: Advantages
# 1. Easy To implement
# 2. There is less distortion in variance

# todo: Disadvantage
# 1. Every situation randomness wont work

# todo: 2. Capturing NAN values with a new feature
# It works well if the data are not missing completely at random 

# todo: loading dataset
df = pd.read_csv('titanic.csv', usecols=['Age', 'Fare', 'Survived'])
df.head()

# todo: create new column which has 1 value if null values present in age column
# this created new column gives some information to model like there was null values in age column
df['Age_NAN'] = np.where(df['Age'].isnull(), 1, 0)
df.head()

# todo: checking median value of column and replacing null values of column with median values
df.Age.median()
df['Age'].fillna(df.Age.median(), inplace=True)
df.head(10)

# todo: Advantages
# 1. Easy to implement
# 2. Captures the importance of missing values

# todo: Disadvantages
# 1. Creating Additional Features(Curse of Dimensionality)

# todo: 3. End of Distribution imputation

# todo: loading data
df = pd.read_csv('titanic.csv', usecols=['Age', 'Fare', 'Survived'])

# todo: analysis dataset
df.head()
df.Age.hist(bins=50)    # create a histogram that has 50 bar

# todo: capturing data of ahead of 3rd standard deviation from mean
extreme = df.Age.mean() + 3 * df.Age.std()

# todo: plotting boxplot
sns.boxplot('Age', data=df)

# todo: function that create feature using end of distribution and median
def impute_nan(df, variable, median, extreme):
    df[variable + "_end_distribution"] = df[variable].fillna(extreme)
    df[variable].fillna(median, inplace=True)

# todo: giving values to function
impute_nan(df, 'Age', df.Age.median(), extreme)

# todo: analysis dataset
df.head()

# todo: creating histogram on age column that has 50 bars
df['Age'].hist(bins=50)

# todo: creating histogram on end of distribution
df['Age_end_distribution'].hist(bins=50)

# todo: creating boxplot of end of distribution
sns.boxplot('Age_end_distribution', data=df)

# todo: advantages
# 1) Capture importance of missingness if there is one

# todo: disadvantage
# 1) Distorts original distribution of the variable.
