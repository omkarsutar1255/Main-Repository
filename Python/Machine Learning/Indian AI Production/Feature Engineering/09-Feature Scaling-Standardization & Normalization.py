# todo: Importing libraries
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# todo: load data
df = sns.load_dataset("titanic")

# todo: analysis dataset
df.head()

# todo: getting some columns from dataset
df2 = df[['survived', "pclass", 'age', 'parch']]
df2.head()

# todo: filling missing values
df3 = df2.fillna(df2.mean())

# todo: Splitting features and labels
X = df3.drop("survived", axis=1)
y = df3["survived"]

# todo: analysis features and labels
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

# todo: Splitting train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

# todo: creating standard scalar
sc = StandardScaler()
sc.fit(X_train)

# todo: analysis data
print(sc.mean_)
print(sc.scale_)
X_train.describe()

# todo: passing train and test data through standard scalar
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)
print(X_train_sc)

# todo: convert 2D array to dataframe
X_train_sc = pd.DataFrame(X_train_sc, columns=["pclass", 'age', 'parch'])
X_test_sc = pd.DataFrame(X_test_sc, columns=["pclass", 'age', 'parch'])

# todo: analysis data
X_train_sc.head()
X_train_sc.describe().round(2)

# todo: creating normalizing scalar
mmc = MinMaxScaler()
mmc.fit(X_train)

# todo: Passing train and test data through normalizing scalar
X_train_mmc = mmc.transform(X_train)
X_test_mmc = mmc.transform(X_test)
print(X_train_mmc)

# todo: converting 2D array into dataframe
X_train_mmc = pd.DataFrame(X_train_mmc, columns=["pclass", 'age', 'parch'])
X_test_mmc = pd.DataFrame(X_test_mmc, columns=["pclass", 'age', 'parch'])

# todo: analysis data using pairplot
X_train_mmc.describe().round(2)
sns.pairplot(X_train)
sns.pairplot(X_train_sc)
sns.pairplot(X_train_mmc)
