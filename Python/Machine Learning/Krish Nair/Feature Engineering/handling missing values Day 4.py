# todo: Ordinal Number Encoding

# todo: import libraries
import datetime
import pandas as pd

# todo: value of datetime
today_date = datetime.datetime.today()
print(today_date)

# todo: getting three days before value
today_date - datetime.timedelta(3)

# todo: list of last 15 days
days = [today_date - datetime.timedelta(x) for x in range(0, 15)]
data = pd.DataFrame(days)   # converting days into dataframe
data.columns = ["Day"]      # giving column name to dataframe column
data.head()

# todo: getting names of weekday
data['weekday'] = data['Day'].dt.weekday_name
data.head()

# todo: 1)label encoding to weekdays
dictionary = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
print(dictionary)

# todo: creating new column that has labels for weekday name
data['weekday_ordinal'] = data['weekday'].map(dictionary)
print(data)

# todo: 2)Count Or Frequency Encoding
train_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', header=None,
                        index_col=None)
train_set.head()

# todo: only getting categorical feature are taking
columns = [1, 3, 5, 6, 7, 8, 9, 13]

# todo: changing dataset to only categorical
train_set = train_set[columns]
# todo: giving column name to dataset column
train_set.columns = ['Employment', 'Degree', 'Status', 'Designation', 'family_job', 'Race', 'Sex', 'Country']
train_set.head()

# todo: showing which column has how many unique categories
for feature in train_set.columns[:]:
    print(feature, ":", len(train_set[feature].unique()), 'labels')

# todo: converting country and value count to dictionary
country_map = train_set['Country'].value_counts().to_dict()

# todo: changing country name to value count in country column of dataset
train_set['Country'] = train_set['Country'].map(country_map)
train_set.head(20)

# todo: Advantages
# 1. Easy To Use
# 2. Not increasing feature space
# todo: Disadvantages
# 1. It will provide same weight if the frequencies are same

# todo: 3)Target Guided Ordinal Encoding
#  (which category has more correlation with target column that will get highest rank)
# 1. Ordering the labels according to the target
# 2. Replace the labels by the joint probability of being 1 or 0

# todo: load dataset
df = pd.read_csv('titanic.csv', usecols=['Cabin', 'Survived'])
df.head()

# todo: creating new category name missing and filling it to null values of cabin column
df['Cabin'].fillna('Missing', inplace=True)

# todo: getting only first letter of cabin name string
df['Cabin'] = df['Cabin'].astype(str).str[0]
df.head()

# todo: show unique values present in cabin column
df.Cabin.unique()

# todo: percentage of getting survived for each unique value of cabin column
df.groupby(['Cabin'])['Survived'].mean()

# todo: getting cabin unique values according to ascending order of their percentage
print(df.groupby(['Cabin'])['Survived'].mean().sort_values().index)
ordinal_labels = df.groupby(['Cabin'])['Survived'].mean().sort_values().index
print(ordinal_labels)

# todo: setting 0, 1, 2,.. values to categories of cabin in not survived manner
enumerate(ordinal_labels, 0)
ordinal_labels2 = {k: i for i, k in enumerate(ordinal_labels, 0)}
print(ordinal_labels2)

# todo: creating new column that ordinal label
df['Cabin_ordinal_labels'] = df['Cabin'].map(ordinal_labels2)
df.head()

# todo: 3)Mean Encoding (Replacing categorical values with their percentage of survived)
mean_ordinal = df.groupby(['Cabin'])['Survived'].mean().to_dict()
print(mean_ordinal)
df['mean_ordinal_encode'] = df['Cabin'].map(mean_ordinal)
df.head()
