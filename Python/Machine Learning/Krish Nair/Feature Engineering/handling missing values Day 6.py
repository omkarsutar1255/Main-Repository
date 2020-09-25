# todo: Transformation of Features or feature scaling

# todo: Why Transformation of Features Are Required?
# 1. Linear Regression---Gradient Descent ----Global Minima
# 2. Algorithms like KNN,K Means,Hierarichal Clustering--- Eucledian Distance

# todo: Every Point has some vectors and Directiom

# Deep Learning Techniques(Standardization, Scaling)
# 1.ANN--->GLobal Minima, Gradient
# 2.CNN
# 3.RNN

# todo: Types Of Transformation
# 1. Normalization And Standardization
# 2. Scaling to Minimum And Maximum values
# 3. Scaling To Median And Quantiles
# 4. gaussian Transformation
#    Logarithmic Transformation
#    Reciprocal Transformation
#    Square Root Transformation
#    Exponential Transformation
#    Box Cox Transformation

# todo: 1)Standardization
# We try to bring all the variables or features to a similar scale. standardisation means centering the variable at zero
# z = (x-x_mean)/std

# todo: importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import scipy.stats as stat
import pylab
import numpy as np

# todo: load dataset
df = pd.read_csv('titanic.csv', usecols=['Pclass', 'Age', 'Fare', 'Survived'])
df.head()

# todo: checking null values in dataset and filling null values with median
df.isnull().sum()
df['Age'].fillna(df.Age.median(), inplace=True)

# todo: standardisation: We use the Standardscalar from sklearn library
scalar = StandardScaler()

# todo: fit vs fit_transform
df_scaled = scalar.fit_transform(df)  # fit uses for train model bt fit transform convert dataset and then train model
print(df_scaled)

# todo: plotting graphs for each column for visualization of distribution after standardisation
plt.hist(df_scaled[:, 1], bins=20)
plt.hist(df_scaled[:, 2], bins=20)
plt.hist(df_scaled[:, 3], bins=20)
plt.hist(df['Fare'], bins=20)

# todo: 2)Min Max Scaling  (CNN)---Deep Learning Techniques
# Min Max Scaling scales the values between 0 to 1.
# X_scaled = (X - X.min / (X.max - X.min)

# todo: transforming dataset to min max scalar
min_max = MinMaxScaler()
df_minmax = pd.DataFrame(min_max.fit_transform(df), columns=df.columns)
df_minmax.head()

# todo: showing visual distribution of columns after min-max scalar
plt.hist(df_minmax['Pclass'], bins=20)
plt.hist(df_minmax['Age'], bins=20)
plt.hist(df_minmax['Fare'], bins=20)

# todo: 3)Robust Scalar
# It is used to scale the feature to median and quantiles
# Scaling using median and quantiles consists of substracting the median to all the observations, and then dividing by
# the interquantile difference. The interquantile difference is the difference between the 75th and 25th quantile:
# IQR = 75% quantile - 25% quantile

# X_scaled = (X - X.median) / IQR

# 0,1,2,3,4,5,6,7,8,9,10
# 9-90 percentile---90% of all values in this group is less than 9
# 1-10 precentile---10% of all values in this group is less than 1
# 4-40%

# todo: Converting dataset into Robust Scalar
scalar = RobustScaler()
df_robust_scaler = pd.DataFrame(scalar.fit_transform(df), columns=df.columns)
df_robust_scaler.head()

# todo: show visual distribution of dataset columns
plt.hist(df_robust_scaler['Age'], bins=20)
plt.hist(df_robust_scaler['Fare'], bins=20)

# todo: 4.1)Gaussian Transformation
# Some machine learning algorithms like linear and logistic assume that the features are normally distributed
# -Accuracy
# -Performance
# - logarithmic transformation
# - reciprocal transformation
# - square root transformation
# - exponential transformation (more general, you can use any exponent)
# - box cox transformation

df = pd.read_csv('titanic.csv', usecols=['Age', 'Fare', 'Survived'])
df.head()

# todo: fill nan
df.isnull().sum()
df['Age'] = df['Age'].fillna(df['Age'].median())


# todo: If you want to check whether feature is guassian or normal distributed use Q-Q plot
def plot_data(df1, feature):
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    df1[feature].hist()
    plt.subplot(1, 2, 2)
    stat.probplot(df1[feature], dist='norm', plot=pylab)
    plt.show()


plot_data(df, 'Age')       # if points are in straight line manner then it is normal distributed

# todo: 4.2)Logarithmic Transformation
df['Age_log'] = np.log(df['Age'])
plot_data(df, 'Age_log')  # if points are not in straight line manner then it cannot use for feature scaling

# todo: 4.3)Reciprocal Transformation
df['Age_reciprocal'] = 1 / df.Age
plot_data(df, 'Age_reciprocal')  # its also not falling in straight line manner so cannot use for feature scaling

# todo: Square Root Transformation
df['Age_sqaure'] = df.Age ** (1 / 2)
plot_data(df, 'Age_sqaure')   # falling in straight manner can use for feature scaling

# todo: Exponential Transdormation
df['Age_exponential'] = df.Age ** (1 / 1.2)
plot_data(df, 'Age_exponential')

# todo: BoxCOx Transformation
# The Box-Cox transformation is defined as:
# T(Y)=(Y exp(λ)−1)/λ
# where Y is the response variable and λ is the transformation parameter. λ varies from -5 to 5. In the transformation,
# all values of λ  are considered and the optimal value for a given variable is selected.

df['Age_Boxcox'], parameters = stat.boxcox(df['Age'])
print(parameters)
plot_data(df, 'Age_Boxcox')   # distribution is normal hence it can use as feature scaling

# todo: Fare
plot_data(df, 'Fare')
df['Fare_log'] = np.log1p(df['Fare'])  # if data has negative values then log1p
plot_data(df, 'Fare_log')

df['Fare_Boxcox'], parameters = stat.boxcox(df['Fare'] + 1)  # converting data into positive by adding 1
plot_data(df, 'Fare_Boxcox')
