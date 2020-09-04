import numpy as np
import pandas as pd

dict1 = {"name": ["harry", "rohan", "omkar", "avdhut"],
         "marks": [345, 754, 1000, 100],
         "city": ["kolkata", "ichalkaranji", "siddhanerli", "kagal"]}
df = pd.DataFrame(dict1)                         # convert dictionary into tables
print(df)
df.to_csv('friends.csv')                         # export data to excel file format
df.to_csv('friends.csv', columns=["tickets", "newcol"])  # export csv file with only two columns
df.to_csv('friends_index_false.csv', index=False)  # if don't want index number in table
df.to_csv('friends_index_false.csv', header=False)  # if don't want header in table
print(df.head(2))                                # to show only first two rows from table
print(df.tail(2))                                # to show only last two rows from table
print(df.describe())                             # gives count, mean, standard deviation, min, max from table
print(df.corr())                                 # used to find pairwise correlation of all columns
print(df.median())                               # gives middle value between max and min values
print(df.shape)                                  # gives shape of table
print(df.info())                                # gives information about dataframe
print(df.notnull())                             # returns booleans values where null values
df.index = ['first', 'second', 'third', 'fourth']  # putting names of indexes
print(df)

print(pd.read_csv('newnewnewnew.csv'))           # to read file that have saved in excel
print(pd.read_csv('newnewnewnew.csv', skiprows=[0, 2]))  # its used to skip any rows from tabel
print(pd.read_csv("newnewnewnew.csv", header=1))    # it will take second row as header of dataframe
print(pd.read_csv("newnewnewnew.csv", header=None, names=["first", "second", "third"]))    # for changed header names
print(pd.read_csv('friends.csv')['marks'])       # to read specific column from table
print(pd.read_csv('friends.csv')['marks'][0])    # to read specific column and row from table
omkar = pd.read_csv('friends.csv')
omkar['marks'][0] = 12                           # to change value of table
print(omkar)                                     # after change values again save it to excel

ser = pd.Series(np.random.rand(27))              # gives random 0-26 numbers in series(column) format
print(ser)
print(type(ser))                                 # gives pandas series type

newdf = pd.DataFrame(np.random.rand(50, 5), index=[np.arange(50)])  # create data frame using numpy and pandas
print(newdf)                                     # also can use head, type, describe
print(newdf.dtypes)                              # gives datatypes of each column
print(newdf.index)                               # gives all index and length of data frame
print(newdf.column)                              # gives starting index, stopping index and step of column
print(newdf.to_numpy())                          # converting table into numpy array
print(newdf.T)                                   # tranverse row and column values
print(newdf.sort_index(axis=1, ascending=False))  # sorting values of columns in descending order
print(newdf[0])
print(type(newdf[0]))                            # gives series type for data frame column
newdf2 = newdf                                   # newdf2 will be view type
newdf2[0][0] = 67.89                             # changes made in view table will also make changes in original table
print(newdf)                                     # changes original array
newdf3 = newdf.copy()                            # create same dataframe by copying original dataframe
newdf3[0][0] = 9.9                               # changes made in new dataframe
print(newdf3)                                    # changes will show in copied dataframe
print(newdf)                                     # changes will not show in original dataframe
newdf.loc[0, 0] = 3.34                           # loc make changes in original dataframe
newdf.columns = list("ABCDE")                    # to give names to column in list form
newdf.loc[0, 0] = 78.56                          # this will create new column of name 0 in dataframe
print(newdf)
print(newdf.drop(4, axis=0))                     # this will remove row of name 4.
print(newdf.drop(0, axis=1))                     # this will remove column of name 0.
print(newdf.loc[[1, 2], ['C', 'D']])             # to view particular dataframe from table
print(newdf.loc[:, ['A', 'B']])                  # use colon to get all rows or column in loc
print(newdf.loc[(newdf['A'] < 0.3)])             # to find out values with condition
print(newdf.loc[(newdf['A'] < 0.3) & (newdf['C'] > 0.1)])  # to find out values with two condition
# if we want to retrieve values in index viz then use iloc where i=index
print(newdf.iloc[0, 0])                          # gives values where index 0 * 0
print(newdf.iloc[[0, 5], [1, 2]])                # gives values where index 0*1, 0*2, 5*1, 5*2
print(newdf.iloc[[True, False, True]])           # this show 0th and 2nd row from dataframe
newdf.drop(['A', 'B'], axis=1, inplace=True)     # to make in original dataframe use inplace=True
print(newdf)
newdf.reset_index(drop=True, inplace=True)       # to reset index from 0 if changed
print(newdf)
print(newdf['B'].isnull())                       # gives True where values are zero
newdf['B'] = None                                # to set any values in any column bt use loc instead of this
print(newdf)

df2 = pd.DataFrame({"name": [pd.NaT, "omkar", "omkar", pd.NaT],
                    "marks": [np.nan, "avdhut", "akshay", "akshat"],
                    "city": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT, "avdhut"]})
print(df2.dropna())                                        # base= copy    # drop rows where is na present
print(df2.dropna(how="all"))                               # base= copy    # drop row if all values have na
print(df2.dropna(how="any"))                               # base= copy    # drop row if any value in dataset is na
print(df2.dropna(how="all", axis=1))                       # base= copy    # drop column if all values have na
print(df2.dropna(how="any", axis=1))                       # base= copy    # drop column if any value in dataset is na
print(df2.drop_duplicates(subset=["name"]))                # base= copy    # drops the duplicates from column
print(df2.drop_duplicates(subset=["name"], keep="first"))  # base= copy    # keep the first record if duplicate
print(df2.drop_duplicates(subset=["name"], keep="last"))   # base= copy    # keep the last record if duplicate
print(df2.drop_duplicates(subset=["name"], keep=False))    # base= copy    # drop record if duplicate
print(df2["name"].value_counts(dropna=False))              # gives counts of unique values and na's

data = pd.read_excel("sheet35.xlsx", sheet_name="Sheet1")  # used to open sheet35 with particular Sheet1 of it
print(data)
data.iloc[0, 0] = 34                                       # made changes in sheet
print(data)
data.to_excel("sheet35.xlsx", sheet_name="Sheet1")         # export changed excel sheet to sheet35
data.to_excel("sheet35.xlsx", sheet_name="Sheet1", startrow=2, startcol=2)  # to give offset to excel file
with pd.ExcelWriter("stoks_weather.xlsx") as writer:  # takes multiple dataframes into multiple sheets of one excel file
    df.to_excel(writer, sheet_name="stocks")
    newdf.to_excel(writer, sheet_name="weather")
