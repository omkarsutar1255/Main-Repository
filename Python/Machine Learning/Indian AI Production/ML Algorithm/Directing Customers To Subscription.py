# Todo: Directing Customers To Subscription Through Financial App Behavior Analysis

# todo: Import essential libraries
import numpy as np  # for numeric calculation
import pandas as pd  # for data analysis and manupulation
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns  # for data visualization
from dateutil import parser  # convert time in date time data type

# todo: Load dataset
fineTech_appData = pd.read_csv("FineTech_appData.csv")
print(fineTech_appData.shape)
fineTech_appData.head(6)  # show first 6 rows of fineTech_appData DataFrame
fineTech_appData.tail(6)  # show last 6 rows of fineTech_appData DataFrame

# todo: Showing first 5 rows from screen list column
for i in [1, 2, 3, 4, 5]:
    print(fineTech_appData.loc[i, 'screen_list'], '\n')

fineTech_appData.isnull().sum()  # take summation of null values
fineTech_appData.info()  # brief inforamtion about Dataset
fineTech_appData.describe()  # give the distribution of numerical variables

# todo: Get the unique value of each columns and it's length
features = fineTech_appData.columns
for i in features:
    print("""Unique value of {}\n{}\nlen is {} \n........................\n
          """.format(i, fineTech_appData[i].unique(), len(fineTech_appData[i].unique())))

# todo: get data type of each columns
print(fineTech_appData.dtypes)

# todo: hour data convert string to int
fineTech_appData['hour'] = fineTech_appData.hour.str.slice(1, 3).astype(int)

# todo: get data type of each columns
print(fineTech_appData.dtypes)

# todo: column names
print(fineTech_appData.columns)

# todo: drop object dtype columns
fineTech_appData2 = fineTech_appData.drop(['user', 'first_open', 'screen_list', 'enrolled_date'], axis=1)
fineTech_appData2.head(6)  # head of numeric dataFrame

# todo: Data visualization

# todo: Heatmap using the correlation matrix
plt.figure(figsize=(16, 9))  # heatmap size in ratio 16:9
sns.heatmap(fineTech_appData2.corr(), annot=True, cmap='coolwarm')  # show heatmap
plt.title("Heatmap using correlation matrix of fineTech_appData2", fontsize=25)  # title of heatmap

# todo: Pailplot of fineTech_appData2 Dataset
sns.pairplot(fineTech_appData2, hue='enrolled')
plt.show()

# todo: Show counterplot of 'enrolled' feature
sns.countplot(fineTech_appData.enrolled)
plt.show()

# todo: value enrolled and not enrolled customers
print("Not enrolled user = ", (fineTech_appData.enrolled < 1).sum(), "out of 50000")
print("Enrolled user = ", 50000 - (fineTech_appData.enrolled < 1).sum(), "out of 50000")

# todo: plot histogram
plt.figure(figsize=(16, 9))  # figure size in ratio 16:9
features = fineTech_appData2.columns  # list of columns name
for i, j in enumerate(features):
    plt.subplot(3, 3, i + 1)  # create subplot for histogram
    plt.title("Histogram of {}".format(j), fontsize=15)  # title of histogram
    bins = len(fineTech_appData2[j].unique())  # bins for histogram
    plt.hist(fineTech_appData2[j], bins=bins, rwidth=0.8, edgecolor="y", linewidth=2, )  # plot histogram
plt.subplots_adjust(hspace=0.5)  # space between horixontal axes (subplots)
plt.show()

# todo: showing all feature from dataset
for i, j in enumerate(features):
    print(i, j)

# todo: Correlation barplot with ‘enrolled’ feature
sns.set()  # set background dark grid
plt.figure(figsize=(14, 5))
plt.title("Correlation all features with 'enrolled' ", fontsize=20)
fineTech_appData3 = fineTech_appData2.drop(['enrolled'], axis=1)  # drop 'enrolled' feature
ax = sns.barplot(fineTech_appData3.columns, fineTech_appData3.corrwith(fineTech_appData2.enrolled))  # plot barplot
ax.tick_params(labelsize=15, labelrotation=20, color="k")  # decorate x &amp; y ticks font

# todo: parsing object datatype into datatime dtype
fineTech_appData['first_open'] = [parser.parse(i) for i in fineTech_appData['first_open']]
fineTech_appData['enrolled_date'] = [parser.parse(i) if isinstance(i, str) else i for i in
                                     fineTech_appData['enrolled_date']]
print(fineTech_appData.dtypes)

# todo: creating new feature that has time of customer used for register for free version
fineTech_appData['time_to_enrolled'] = (fineTech_appData.enrolled_date - fineTech_appData.first_open).astype(
    'timedelta64[h]')
plt.hist(fineTech_appData['time_to_enrolled'].dropna())
plt.show()
plt.hist(fineTech_appData['time_to_enrolled'].dropna(), range=(0, 100))
plt.show()

# todo: Those customers have enrolled after 48 hours set as 0
fineTech_appData.loc[fineTech_appData.time_to_enrolled > 48, 'enrolled'] = 0
print(fineTech_appData)

# todo: droping new created features
fineTech_appData.drop(columns=['time_to_enrolled', 'enrolled_date', 'first_open'], inplace=False)
print(fineTech_appData)

# todo: read csv file and convert it into numpy array
fineTech_app_screen_Data = pd.read_csv("top_screens.csv").top_screens.values
print(fineTech_app_screen_Data)
type(fineTech_app_screen_Data)

# todo: Add ',' at the end of each string of 'screen_list' for further operation.
fineTech_appData['screen_list'] = fineTech_appData.screen_list.astype(str) + ','
print(fineTech_appData)

# todo: string into to number
for screen_name in fineTech_app_screen_Data:
    fineTech_appData[screen_name] = fineTech_appData.screen_list.str.contains(screen_name).astype(int)
    fineTech_appData['screen_list'] = fineTech_appData.screen_list.str.replace(screen_name + ",", "")

# todo: test
fineTech_appData.screen_list.str.contains('Splash').astype(int)
fineTech_appData.screen_list.str.replace('Splash' + ",", "")

print(fineTech_appData.shape)
print(fineTech_appData.head(6))
print(fineTech_appData.screen_list.str.count(",").head(6))

# todo: remain screen in 'screen_list'
print(fineTech_appData.loc[0, 'screen_list'])

# todo: count remain screen list and store counted number in 'remain_screen_list'
fineTech_appData['remain_screen_list'] = fineTech_appData.screen_list.str.count(",")

# todo: Drop the 'screen_list'
fineTech_appData.drop(columns=['screen_list'], inplace=False)

# todo: total columns
print(fineTech_appData)
print(fineTech_appData.columns)

# todo: take sum of all saving screen in one place
saving_screens = ['Saving1',
                  'Saving2',
                  'Saving2Amount',
                  'Saving4',
                  'Saving5',
                  'Saving6',
                  'Saving7',
                  'Saving8',
                  'Saving9',
                  'Saving10']
fineTech_appData['saving_screens_count'] = fineTech_appData[saving_screens].sum(axis=1)
fineTech_appData.drop(columns=saving_screens, inplace=False)
print(fineTech_appData)

credit_screens = ['Credit1',
                  'Credit2',
                  'Credit3',
                  'Credit3Container',
                  'Credit3Dashboard']
fineTech_appData['credit_screens_count'] = fineTech_appData[credit_screens].sum(axis=1)
fineTech_appData.drop(columns=credit_screens, axis=1, inplace=False)
print(fineTech_appData)

cc_screens = ['CC1',
              'CC1Category',
              'CC3']
fineTech_appData['cc_screens_count'] = fineTech_appData[cc_screens].sum(axis=1)
fineTech_appData.drop(columns=cc_screens, inplace=False)
print(fineTech_appData)

loan_screens = ['Loan',
                'Loan2',
                'Loan3',
                'Loan4']
fineTech_appData['loan_screens_count'] = fineTech_appData[loan_screens].sum(axis=1)
fineTech_appData.drop(columns=loan_screens, inplace=False)
print(fineTech_appData)

print(fineTech_appData.shape)
print(fineTech_appData.info())
print(fineTech_appData.describe())

# todo: Heatmap with correlation matrix of new fineTech_appData
plt.figure(figsize=(25, 16))
sns.heatmap(fineTech_appData.corr(), annot=True, linewidth=2)  # *****code 13
plt.show()

print(fineTech_appData.columns)
fineTech_appData['ProfileChildren '].unique()

corr_matrix = fineTech_appData.corr()
print(corr_matrix['ProfileChildren '])
print(fineTech_appData['ProfileChildren '])

# todo: Data Preprocessing

# todo: Split dataset in features and target
clean_fineTech_appData = fineTech_appData
target = fineTech_appData['enrolled']
fineTech_appData.drop(columns='enrolled', inplace=False)

# todo: Split dataset in Train and Test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(fineTech_appData, target, test_size=0.2, random_state=0)
print('Shape of X_train = ', X_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of y_test = ', y_test.shape)

# todo: take User ID in another variable
train_userID = X_train['user']
X_train.drop(columns='user', inplace=False)
test_userID = X_test['user']
X_test.drop(columns='user', inplace=False)

print('Shape of X_train = ', X_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of train_userID = ', train_userID.shape)
print('Shape of test_userID = ', test_userID.shape)

# todo: Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

# todo: Model Building
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# todo: Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(criterion='entropy', random_state=0)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
accuracy_score(y_test, y_pred_dt)

# todo: train with Standard Scaling dataset
dt_model2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
dt_model2.fit(X_train_sc, y_train)
y_pred_dt_sc = dt_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_dt_sc)

# todo: K-NN
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2, )
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
accuracy_score(y_test, y_pred_knn)

# todo: train with Standard Scaling dataset
knn_model2 = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2, )
knn_model2.fit(X_train_sc, y_train)
y_pred_knn_sc = knn_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_knn_sc)

# todo: Naive Bayes
from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
accuracy_score(y_test, y_pred_nb)

# todo: train with Standard Scaling dataset
nb_model2 = GaussianNB()
nb_model2.fit(X_train_sc, y_train)
y_pred_nb_sc = nb_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_nb_sc)

# todo: Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
accuracy_score(y_test, y_pred_rf)

# todo: train with Standard Scaling dataset
rf_model2 = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
rf_model2.fit(X_train_sc, y_train)
y_pred_rf_sc = rf_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_rf_sc)

# todo: Logistic Regression
from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(random_state=0, penalty='l1')
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
accuracy_score(y_test, y_pred_lr)

# todo: train with Standard Scaling dataset
lr_model2 = LogisticRegression(random_state=0, penalty='l1')
lr_model2.fit(X_train_sc, y_train)
y_pred_lr_sc = lr_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_lr_sc)

# todo: Support Vector Machine
from sklearn.svm import SVC

svc_model = SVC()
svc_model.fit(X_train, y_train)
y_pred_svc = svc_model.predict(X_test)
accuracy_score(y_test, y_pred_svc)

# todo: train with Standard Scaling dataset
svc_model2 = SVC()
svc_model2.fit(X_train_sc, y_train)
y_pred_svc_sc = svc_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_svc_sc)

"""from sklearn.svm import SVC
grid_para = {'C': [1, 10, 100], 'gamma': [1, 0.01, 0.001], 'kernel': ['rbf']}
from sklearn.model_selection import GridSearchCV
grid_lr = GridSearchCV(SVC(), param_grid=grid_para, refit=True, verbose=4, n_jobs=-1)
grid_lr.fit(X_train, y_train)
grid_pred_lr = grid_lr.predict(X_test)
cm_grid_lr = confusion_matrix(y_test, grid_pred_lr)
sns.heatmap(cm_grid_lr, annot=True, fmt='g')
accuracy_score(y_test, grid_pred_lr)"""

# todo: XGBoost Classifier
from xgboost import XGBClassifier
xgb_model = XGBClassifier()
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)
accuracy_score(y_test, y_pred_xgb)

# todo: train with Standard Scaling dataset
xgb_model2 = XGBClassifier()
xgb_model2.fit(X_train_sc, y_train)
y_pred_xgb_sc = xgb_model2.predict(X_test_sc)
accuracy_score(y_test, y_pred_xgb_sc)

# todo: XGB classifier with parameter tuning
xgb_model_pt1 = XGBClassifier(
    learning_rate=0.01,
    n_estimators=5000,
    max_depth=4,
    min_child_weight=6,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.005,
    objective='binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27)
xgb_model_pt1.fit(X_train, y_train)
y_pred_xgb_pt1 = xgb_model_pt1.predict(X_test)
accuracy_score(y_test, y_pred_xgb_pt1)

# todo: XGB classifier with parameter tuning and train with Standard Scaling dataset
xgb_model_pt2 = XGBClassifier(
    learning_rate=0.01,
    n_estimators=5000,
    max_depth=4,
    min_child_weight=6,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.005,
    objective='binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27)
xgb_model_pt2.fit(X_train_sc, y_train)
y_pred_xgb_sc_pt2 = xgb_model_pt2.predict(X_test_sc)
accuracy_score(y_test, y_pred_xgb_sc_pt2)

# todo: confussion matrix
cm_xgb_pt2 = confusion_matrix(y_test, y_pred_xgb_sc_pt2)
sns.heatmap(cm_xgb_pt2, annot=True, fmt='g')
plt.title("Confussion Matrix", fontsize=20)  # *****code 14

# todo: Clasification Report
cr_xgb_pt2 = classification_report(y_test, y_pred_xgb_sc_pt2)
print("Classification report >>> \n", cr_xgb_pt2)

# todo: Cross validation
from sklearn.model_selection import cross_val_score
cross_validation = cross_val_score(estimator=xgb_model_pt2, X=X_train_sc, y=y_train, cv=10)
print("Cross validation of XGBoost model = ", cross_validation)
print("Cross validation of XGBoost model (in mean) = ", cross_validation.mean())

# todo: Mapping predicted output to the target
final_result = pd.concat([test_userID, y_test], axis=1)
final_result['predicted result'] = y_pred_xgb_sc_pt2
print(final_result)

# todo: Save the Model Using Pickle
import pickle

# todo: save model
pickle.dump(xgb_model_pt2, open('FineTech_app_ML_model.pickle', 'wb'))

# todo: load model
ml_model_pl = pickle.load(open('FineTech_app_ML_model.pickle', 'rb'))

# todo: predict the output
y_pred_pl = ml_model_pl.predict(X_test_sc)

# todo: confusion matrix
cm_pl = confusion_matrix(y_test, y_pred_pl)
print('Confussion matrix = \n', cm_pl)

# todo: show the accuracy
print("Accuracy of model = ", accuracy_score(y_test, y_pred_pl))

# todo: Save the Model Using Joblib
import joblib

# todo: save model
joblib.dump(xgb_model_pt2, 'FineTech_app_ML_model.joblib')

# todo: load model
ml_model_jl = joblib.load('FineTech_app_ML_model.joblib')

# todo: predict the output
y_pred_jl = ml_model_jl.predict(X_test_sc)

# todo: confusion matrix
cm_jl = confusion_matrix(y_test, y_pred_jl)
print('Confussion matrix = \n', cm_jl)

# todo: show the accuracy
print("Accuracy of model = ", accuracy_score(y_test, y_pred_jl))
