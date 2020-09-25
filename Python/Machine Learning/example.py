"""
import pandas as pd
modeexam = pd.read_csv("new data.csv")
# print(modeexam.keys())
print("most coming value is 5.713")
# mode() give most coming value in column and [0] get first value from mode().
print(modeexam['RM'].mode()[0])

# jupyter nbconvert --to script  to convert jupyter file to python file

# mode operation can perform on string values
df = pd.Series(['omkar', 'suat', 'omakr', 'hello', 'hi', 'go', 'omkar', 'miss', 'can', 'tell'])
print(df.mode())

a = ["omklar", "sutar"]
b = a
print(b)

z = ['omkar', 'suat', 'omakr', 'hello', 'hi', 'go', 'omkar', 'miss', 'can', 'tell']
for a in range(2):
    y = z
    x = y.copy()
    print(y)
    print(x)
    print(z)

import pandas as pd
df3 = pd.read_csv("Worker2.csv")
# df4 = pd.get_dummies(df3, columns=['sex', 'name'], drop_first=False)
print(df3)
# print(df4)
df5 = pd.get_dummies(df3, columns=['sex', 'name', 'sex'], drop_first=True)
print(df5.columns)
final_df = df5.loc[:, ~df5.columns.duplicated()]
print(final_df.columns)"""
