# todo: Discussion Related With Outliers And Impact On Machine Learning!!

# todo: Which Machine LEarning Models Are Sensitive To Outliers?
# 1. Naivye Bayes Classifier--- Not Sensitive To Outliers
# 2. SVM--------                Not Sensitive To Outliers          
# 3. Linear Regression----------  Sensitive To Outliers
# 4. Logistic Regression-------   Sensitive To Outliers
# 5. Decision Tree Regressor or Classifier---- Not Sensitive
# 6. Ensemble(RF,XGboost,GB)------- Not Sensitive
# 7. KNN--------------------------- Not Sensitive 
# 8. Kmeans------------------------ Sensitive
# 9. Hierarichal------------------- Sensitive 
# 10. PCA-------------------------- Sensitive 
# 11. Neural Networks-------------- Sensitive

# todo: import libraries
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# todo: load dataset
df = pd.read_csv('titanic.csv')
df.head()

# todo: null values in age column
df['Age'].isnull().sum()

# todo: plotting seaborn with handling missing values in age column
sns.distplot(df['Age'].dropna())
sns.distplot(df['Age'].fillna(100))

# todo: plotting histogram of age column (showing gaussian distribution)
figure = df.Age.hist(bins=50)
figure.set_title('Age')
figure.set_xlabel('Age')
figure.set_ylabel('No of passenger')

# todo: plotting boxplot
figure = df.boxplot(column="Age")
df['Age'].describe()

# todo: If The Data Is Normally Distributed We use this
# todo: Assuming Age follows A Gaussian Distribution we will calculate the boundaries which differentiates the outliers
uppper_boundary = df['Age'].mean() + 3 * df['Age'].std()
lower_boundary = df['Age'].mean() - 3 * df['Age'].std()
print(lower_boundary), print(uppper_boundary), print(df['Age'].mean())

# todo: If Features Are Skewed We Use the below Technique
figure2 = df.Fare.hist(bins=50)
figure2.set_title('Fare')
figure2.set_xlabel('Fare')
figure2.set_ylabel('No of passenger')

# todo: plotting boxplot
df.boxplot(column="Fare")
df['Fare'].describe()

# todo: Lets compute the Interquantile range to calculate the boundaries
IQR = df.Fare.quantile(0.75) - df.Fare.quantile(0.25)

# todo: calculating outlier boundaries
lower_bridge = df['Fare'].quantile(0.25) - (IQR * 1.5)
upper_bridge = df['Fare'].quantile(0.75) + (IQR * 1.5)
print(lower_bridge), print(upper_bridge)

# todo: Calculating extreme outliers boundaries
lower_bridge = df['Fare'].quantile(0.25) - (IQR * 3)
upper_bridge = df['Fare'].quantile(0.75) + (IQR * 3)
print(lower_bridge), print(upper_bridge)

data = df.copy()
data.loc[data['Age'] >= 73, 'Age'] = 73       # If "Age" value is greater than 73 then replace it with 73
data.loc[data['Fare'] >= 100, 'Fare'] = 100   # If "Fare" value is greater than 100 then replace it with 100

# todo: Plotting Age column after replacing outlier
figure3 = data.Age.hist(bins=50)
figure3.set_title('Age')
figure3.set_xlabel('Age')
figure3.set_ylabel('No of passenger')

# todo: plotting Fare column after replacing outlier
figure4 = data.Fare.hist(bins=50)
figure4.set_title('Fare')
figure4.set_xlabel('Fare')
figure4.set_ylabel('No of passenger')

# todo: splitting into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(data[['Age', 'Fare']].fillna(0), data['Survived'], test_size=0.3)

# todo: Logistic Regression
classifier1 = LogisticRegression()
classifier1.fit(X_train, y_train)
y_pred = classifier1.predict(X_test)
y_pred1 = classifier1.predict_proba(X_test)  # returns probability of getting -1 and 1

print(f"Accuracy_score: {accuracy_score(y_test, y_pred)}")
print(f"roc_auc_score: {roc_auc_score(y_test, y_pred1[:, 1])}")
# if we give y_test and y_pred with positive values then roc_auc_score calculate accuracy of curve of classification

# todo: Random Forest Classifier
classifier2 = RandomForestClassifier
classifier2.fit(X=X_train, y=y_train)
y_pred = classifier2.predict(X=X_test)
y_pred1 = classifier2.predict_proba(X=X_test)
print(f"Accuracy_score: {accuracy_score(y_test, y_pred)}")
print(f"roc_auc_score: {roc_auc_score(y_test, y_pred1[:, 1])}")
