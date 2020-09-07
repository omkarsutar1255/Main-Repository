import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlalchemy

# ========1. INTRODUCTION TO PANDAS==========
df = pd.DataFrame(np.random.rand(7, 3))
df.iloc[0, 0] = pd.NaT
df.fillna(0, inplace=True)                       # to add value to empty position (data muglling or wragging)

# ========2. DATAFRAME BASICS===============
df = df.rename(columns={2: "temp"})              # to rename the column name
print(df["temp"][df.temp == df["temp"].max()])   # where temp column max value, gives row, then selected temp column
df.set_index(3, inplace=True)                             # to set any column to index
print(df)
df = df.loc[6]                     # to get row information of index 6
print(df)

# ===========3. CREATING DATAFRAMES=============
# creating a dataframe can be done by following things:
# 1)using csv, 2)using Excel, 3)from python dictionary, 4)from list of tuples, 5)from list of dictionaries
weather_data = [                                             # this is way to create dataframe using tupple
    ("1/1/2018", 546, "rain"),
    ("3/4/2019", 453, "sunny"),
    ("5/7/2020", 56, "water")]
df = pd.DataFrame(weather_data, columns=["day", "temperature", "event"])
print(df)

# ============4. READ WRITE EXCEL CSV FILES===============
df2 = pd.read_csv("newnewnewnew.csv", na_values=["not available", -1.1, "n.a."]) # this is use to clean data of csv file
# it sets the NaN values changing specific values from table
df3 = pd.read_csv("newnewnewnew.csv", names={"apps": ["not available", "n.a."], "things": [-1.1, "n.a."]})
# this is the way we can remove specific values from specific columns
def convert_people_cell(cell):
    if cell == "n.a.":
        return "sam walton"
    return cell
df4 = pd.read_excel("sheet35.xlsx", "Sheet", converters={"people": convert_people_cell})
print(df4)             # create a function that we do specific works and use to to converters to make changes in file

# ==========5. HANDLE MISSING DATA:fillna, dropna, interpolate==============
parse_dates = ["day"]    # this convert date into 2017-01-11 format while reading csv file
df.fillna(method="ffill")        # this fill na values with previous valeus in table
df.fillna(method="bfill")        # this fill na values with next valeus in table
# we can add axis=1 and limit=1 for copying values
df.fillna({"name": "none", "sutar": 0})  # filling different values in different columns with replacing na values
df.interpolate()            # this fill na values with center values between next and previous values
# here we can ues method= "time" so can put na values according to time
# method = "index" will fill values index wise
df.interpolate(method="nearest")          # put nearest from next and previous values in na values
df.interpolate(limit=1, limit_direction="backward")  # only one time it will interpolate values and also in backward way
df.interpolate(limit=1, limit_direction="both")  # only one time it will interpolate values but in both direction

df.dropna(thresh=2)         # this means row should have min 2 valid values otherwise row will drop
pd.date_range("01-01-2020", "11-01-2020")  # this gives all dates between two dates
pd.DatetimeIndex()                         # this set datetime index
df.reindex()                               # this change the original index with new one

# ==============6. replace function==============
df.replace([-999.9, -9888.9], np.NaN)      # replace two values of data with nan value
df.replace([-999.9, -9888.9], ["new1", "new2"])      # replace values of data with new values
df.replace({"zeros": -999.9, "without_zeros": 0}, np.NaN)  # replace specific values from specific columns with nan
df.replace({-999.9: np.NaN})               # this directly replaced values from table
regex = True               # use regex in replace find particular part of word from any values and replace it
# we can give A-Za-z0-9 like parameters in regex
df.replace("health", method="ffill")           # replace health word with its previous value
df.replace(0, method="bfill", limit=2)           # replace 0 with its next value but only 2 times

# ==============7. GROUP BY==================
df = pd.read_csv("temperature")
g = df.groupby("city")                            # to group by similar names of city column
for city, city_df in g:
    print(city)                                   # group names
    print(city_df)                                # dataframes in each group
print(g.get_group("mumbai"))                      # to iterate specific group
print(g.max())                                    # to get max, min, mean, average, sum, describe values from each group
print(g.agg(["sum", "max", "mean"]))              # retrieve sum, max, mean of groupby in a single table
f = g.get_group("mumbai")
f.plot.line()                            # gives graphical representation in lines of dataframe
plt.show()

# =============8. CONCAT DATAFRAMES===============
df = pd.concat([df, df2, df3, df4], ignore_index=True)   # concat various dataframes in one
print(df)                                               # ignore_index=True is delete previous index and add new index
df = pd.concat([df, city_df], keys=["india", "usa"])          # concat dataframes with attach keys to each dataframes
print(df.loc["india"])                                       # to print particular dataframe from concat dataframe
axis = 1                                      # axis 1 concat dataframes in horizontal way
index = [1, 0]                                # while create dataframe use index
# so when concat this dataframe with other it should change dataframe order according to concat index
s = pd.Series(["humid", "dry", "rain"], name="event")         # this create new dataframe
df = pd.concat([temperatue, s], axis=1)                       # adding new dataframe to temperature dataframe
print(df)
df5 = pd.concat([df2, df3], axis=1, join="inner")             # inner will concat common indexes from two dataframes
df6 = pd.concat([df2, df3], axis=1, ignore_index=df2.index)   # this will concat dataframes based on df3 indexes
df7 = pd.concat([df2, df3], axis=1, keys=["1st", "2nd"])         # this show 1st, 2nd names on both dataframes
df8 = pd.concat([df2, df3], sort=False)                          # if two dataframes don't have same columns
# then it will show nan values but if sort=False then program will not give warning

# =============9. MERGE DATAFRAMES==============
dict1 = {"name": ["harry", "rohan", "omkar", "avdhut"],
         "marks": [345, 754, 1000, 100]}
df1 = pd.DataFrame(dict1)
dict2 = {"name": ["harry", "rohan", "omkar", "avdhut"],
         "city": ["kolkata", "ichalkaranji", "siddhanerli", "kagal"]}
df2 = pd.DataFrame(dict2)
df3 = pd.merge(df1, df2, on="name", how="inner")      # merge two dataframes into one with taking same column as index
print(df3)                          # inner gives common rows between them
# outer gives all rows from two dataframes
# left gives all rows of first dataframes and matching rows from second dataframes
# right gives all rows of second dataframes and matching rows from first dataframes
df3 = pd.merge(df1, df2, on="name", how="inner", indicator=True)
# after merging it indicates which data comes from which dataframes
# and for same column from both dataframes we can give suffixes=("_first", "_second")
M = pd.merge(df1, df2, left_index=True, right_index=True)
# while merge two dataframe if we have different index then above method will give separate index after merge

# ===============10. PIVOT TABLE===================
df1.pivot(index="date", columns="city", values="temperature")  # setting rows and column from dataframes
# values retrieve only temperature results from table
df1.pivot_table(index=pd.Grouper(freq="M", key="date"), columns="city")
# grouping the data according to months from date
df1.pivot_table(index="date", columns="city", aggfunc="count")  # we can use max, sum as aggfunc
# this gives counts same values in table where rows are date and columns are cityname
df1.pivot_table(index="date", columns="city", fill_value=0)    # replace nan value with 0
# here dropna=True means if all value in any column are nan then that column will drop\
df1.pivot_table(index="date", columns="city", margins=True)
# margin gives average(bydefault:aggfunc="mean") or max or min or sum value of all values in rows and columns

# ==============11. RESHAPE DATAFRAMES USING MELT==============
df2 = pd.melt(df1, id_vars=["day"], var_name="city", value_name="temp")
# convert data into giving date for each value of dataframe plus giving column names

# ================12. STACK UNSTACK==============
df4 = df1.stack(level=0)   # this take first row for stack otherwise second row will stack
df5 = df4.unstack()        # to unstack stacked dataframe
# if we have three header and within that if we want first row will stack then level=0
# if we want second row to transform then level=1
# if we want third row to transform then level=2
# while reading excel file header=[0, 1, 2] for perform level operation to transform

# ===============13. CROSSTAB===================
df6 = pd.crosstab([df1.row_name], [df1.columns_name], margins=True)  # margin gives sum of counts
# we can pass two column_name or two row_name in list format for different output
# we can pass normalize="index" in crosstab for get percentage of value with total
pd.crosstab([df5.sex], [df6.handiness], values=df5.age, aggfunc=np.average)
# this gives average of age of which fits in each row*column category

# =========14. READ WRITE DATA FROM DATABASE=============
engine = sqlalchemy.create_engine("mysql+pymysql://root:tiger@localhost:3306/omkar")
df7 = pd.read_sql_table("employee", con=engine)
print(df7)

# =========TIME SERIES ANALYSIS PART 1: DATETIMEINDEX AND RESHAPE===========
df9 = pd.read_csv("aapl.csv", parse_dates=["Date"], index_col="Date")
# convert the date from str to datetime and index_col will set date as index
df9.head()
type(df9.Date[0])
df10 = df9["2017"].close.mean()    # close is column name which we want to retrieve from 2017
# mean will give mean of all values from close column
g = df9.close.reshape("M").mean()      # to get month wise mean of close column
g.plot.line()                          # to convert data into line graph
plt.show()                             # we can use kind="bar" to get histogram graph

# ======== DATA RANGE ============
# read csv file in df10
rng = pd.date_range(start="1/1/2020", end="30/1/2020", freq="B")
# adding date to any dataframes with particular range and frequency(B=Business)
# we can set date as index using set index method
# we can retrieve particular date by mentioning list[:] format
df11 = df4.asfreq("w", method="pad")
# in this type we can set freq and "pad" is used to pass on the previous values
ts = pd.Series(np.random.randint(1, 10, len(df7)), index=df7)
# we can create series of len(df7) much of random number between 1 to 10 and set then with index

# ==========TIME SERIES ANALYSIS 3: HOLIDAYS =============
# watch video of codebasics

# ==========TO_DATETIME===============
# we can use format method to convert any type of date to standard datetime
# in datetime we first pass string of dates and then error="coerce" or unit="s" for seconds

# ============PD.PERIOD AND PD.PERIODINDEX MODULES===============
# if we give pd.period with month, year, week, day then this will give you start and end of period time

# ============TIMEZONE=============
# this is use to deal with various time at various countries

# ============TIME SERIES: SHIFTING AND LAGGING==============
# this shift any columns all values with some places in downward direction
