# todo: Missing Values- Feature Engineering- Day 1

# todo: Lifecycle of a Data Science Projects
# 1. Data Collection Statergy---from company side,3rd party APi's,Surveys,Surveys
# 2. Feature Engineering---Handling Missing Values

# todo: Why are their Missing values?? Survey--Depression Survey
# 1. They hesitate to put down the information
# 2. Survey informations are not that valid
# 3. Men--salary
# 4. Women---age
# 5. People may have died----NAN

# todo: Data Science Projects---Dataset should be collected from multiple sources

# todo: What are the different types of Missing Data?
# 
# todo: 1. Missing Completely at Random, MCAR:
# A variable is missing completely at random (MCAR) if the probability of being missing is the same for all the
# observations. When data is MCAR, there is absolutely no relationship between the data missing and any other values,
# observed or missing, within the dataset. In other words, those missing data points are a random subset of the data.
# There is nothing systematic going on that makes some data more likely to be missing than other.

# todo: import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# todo: load dataset
df = pd.read_csv('titanic.csv')

# todo: analysis dataset
df.head()
df.isnull().sum()

print(df[df['Embarked'].isnull()])

# todo: 2. Missing Data Not At Random(MNAR): Systematic missing Values
# There is absolutely some relationship between the data missing and any other values,
# observed or missing, within the dataset.

# todo: creating new column if cabin column has null values then new column has 1 value respectively.
df['cabin_null'] = np.where(df['Cabin'].isnull(), 1, 0)

# todo: find the percentage of null values
df['cabin_null'].mean()

print(df.columns)

# todo: show what percentage of survived person has null values in cabin column
df.groupby(['Survived'])['cabin_null'].mean()

# todo: Missing At Random(MAR)
# Men---hide their salary
# Women---hide their age

# todo: All the techniques of handling missing values
# 1. Mean/ Median/Mode replacement
# 2. Random Sample Imputation
# 3. Capturing NAN values with a new feature
# 4. End of Distribution imputation
# 5. Arbitrary imputation
# 6. Frequent categories imputation

# todo: Mean/ Median /Mode imputation
# When should we apply?
# Mean/median imputation has the assumption that the data are missing completely at random(MCAR).
# We solve this by replacing the NAN with the most frequent occurrence of the variables

# todo: load dataset
df = pd.read_csv('titanic.csv', usecols=['Age', 'Fare', 'Survived'])
df.head()

# todo: Lets go and see the percentage of missing values
df.isnull().mean()

# todo: function that put median value at null values
def impute_nan(df, variable, median):
    df[variable + "_median"] = df[variable].fillna(median)

# todo: checking what is median value of column
median = df.Age.median()
print(median)

# todo: calling function with dataset, column and strategy
impute_nan(df, 'Age', median)

# todo: analysis dataset
df.head()
print(df['Age'].std())
print(df['Age_median'].std())

# todo: check distribution of dataset in graphical manner
fig = plt.figure()
ax = fig.add_subplot(111)
df['Age'].plot(kind='kde', ax=ax)
df.Age_median.plot(kind='kde', ax=ax, color='red')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')

# todo: Advantages And Disadvantages of Mean/Median Imputation
# todo: Advantages
# 1. Easy to implement(Robust to outliers)
# 2. Faster way to obtain the complete dataset
# todo: Disadvantages
# 1. Change or Distortion in the original variance
# 2. Impacts Correlation
