# todo: Label encoding & Ordinal Encoding

# todo: importing libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder  # OrdinalEncoder

# todo: to show all rows in output
pd.set_option("display.max_rows", None)

# todo: reading dataset
df = pd.read_csv(r"G:\DataSet\House Price Prediction\train.csv")

# todo: analysing dataset
df.head()

# todo: selecting some columns to Label encode
df2 = df[["KitchenQual", "BldgType"]]

# todo: creating object of Label encoder
le = LabelEncoder()

# todo: passing one column of dataset in label encoding
le.fit_transform(df2["BldgType"])

# todo: creating new column of label encoding
df2["BldgType_L_enc"] = le.fit_transform(df2["BldgType"])
print(df2)

# todo: analysis columns
df["BldgType"].value_counts()
df["KitchenQual"].value_counts()

"""
KitchenQual: Kitchen quality
Ex	Excellent
Gd	Good
TA	Typical/Average
Fa	Fair
"""

# todo: label encoding by assigning number manual
order_Label = {"Ex": 4, "Gd": 3, "TA": 2, "Fa": 1}
df2["KitchenQual_org_enc"] = df2["KitchenQual"].map(order_Label)
print(df2)
