# todo: Categorical Variable Encoding
# todo: Dummy Variables & One-Hot Encoding

# todo: importing libraries
import pandas as pd 

# loading data as tips_df
tips_df = pd.read_csv(r"C:/Users/kashz/seaborn-data/tips.csv")
print(tips_df)

# todo: creating dummy variable from dataset
dummy_df = pd.get_dummies(tips_df)
print(dummy_df)

# pd.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False,
#                dtype=None, ) -> 'DataFrame'
# todo: creating dummy variable with dropping one column
pd.get_dummies(tips_df, drop_first=True, columns=None)  # in column we can specify column names

# todo: One-Hot Encoding with Scikit-learn
from sklearn.preprocessing import OneHotEncoder
oh_enc = OneHotEncoder(sparse=False, drop="First")

# todo: passing columns of dataset to create dummy variables
oh_enc_arr = oh_enc.fit_transform(tips_df[['sex', 'smoker', 'day', 'time']])
print(oh_enc_arr)   # it returns 2D array

dummy_df.keys()

# todo: giving names to 2D array of dummy variable and converting it to dataframe
oh_enc_df = pd.DataFrame(oh_enc_arr, columns=['sex_Female', 'sex_Male', 'smoker_No',
       'smoker_Yes', 'day_Fri', 'day_Sat', 'day_Sun', 'day_Thur',
       'time_Dinner', 'time_Lunch'])
print(oh_enc_df)
