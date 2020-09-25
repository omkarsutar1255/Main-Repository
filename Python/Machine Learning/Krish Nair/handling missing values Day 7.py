# todo: Feature Selection Techniques

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import mutual_info_classif

df = pd.read_csv('mobile_dataset.csv')
df.head()

# todo: Univariate Selection

X = df.iloc[:, :-1]
y = df['price_range']

X.head()

y.head()

print(df.shape)

# todo: Apply SelectKBest Algorithm
ordered_rank_features = SelectKBest(score_func=chi2, k=20)
ordered_feature = ordered_rank_features.fit(X, y)

dfscores = pd.DataFrame(ordered_feature.scores_, columns=["Score"])
dfcolumns = pd.DataFrame(X.columns)

features_rank = pd.concat([dfcolumns, dfscores], axis=1)

features_rank.columns = ['Features', 'Score']
print(features_rank)

features_rank.nlargest(10, 'Score')

# todo: Feature Importance
# This technique gives you a score for each feature of your data,the higher the score mor relevant it is

model = ExtraTreesClassifier()
model.fit(X, y)

print(model.feature_importances_)

ranked_features = pd.Series(model.feature_importances_, index=X.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()

# todo: Correlation

df.corr()


corr = df.iloc[:, :-1].corr()
top_features = corr.index
plt.figure(figsize=(20, 20))
sns.heatmap(df[top_features].corr(), annot=True)

# todo: Remove The correlated

threshold = 0.8


# find and remove correlated features
def correlation(dataset, threshold1):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold1:  # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr


correlation(df.iloc[:, :-1], threshold)

# todo: Information Gain

mutual_info = mutual_info_classif(X, y)

mutual_data = pd.Series(mutual_info, index=X.columns)
mutual_data.sort_values(ascending=False)
