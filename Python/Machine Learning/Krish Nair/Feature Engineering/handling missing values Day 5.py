# todo: Probability Ratio Encoding
# 1. Probability of Survived based on Cabin--- Categorical Feature
# 2. Probability of Not Survived---1-pr(Survived)
# 3. pr(Survived)/pr(Not Survived)
# 4. Dictonary to map cabin with probability
# 5. replace with the categorical feature

# todo: import libraries
import pandas as pd

# todo: load dataset
df = pd.read_csv('titanic.csv', usecols=['Cabin', 'Survived'])
df.head()

# todo: filling null values as "missing"
df['Cabin'].fillna('Missing', inplace=True)
df.head()

# todo: getting categories name of cabin column
df['Cabin'].unique()

# todo: getting only first character of category name
df['Cabin'] = df['Cabin'].astype(str).str[0]
df.head()
df.Cabin.unique()

# todo: show percentage of cabin categories survived
prob_df = df.groupby(['Cabin'])['Survived'].mean()

# todo: converting prob_df into dataframe
prob_df = pd.DataFrame(prob_df)
print(prob_df)

# todo: creating column died by minus survived value with from 1
prob_df['Died'] = 1 - prob_df['Survived']
prob_df.head()

# todo: calculating probability ratio(survived/died)
prob_df['Probability_ratio'] = prob_df['Survived'] / prob_df['Died']
prob_df.head()

# todo: convert probability ratio to dict
probability_encoded = prob_df['Probability_ratio'].to_dict()

# todo: replace cabin values with probability ratio values
df['Cabin_encoded'] = df['Cabin'].map(probability_encoded)
df.head()
df.head(20)
