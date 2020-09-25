import pandas as pd
import datetime

# create a variable with dates, and from that extract the weekday
# I create a list of dates with 20 days difference from today
# and then transform it into a dataframe
df_base = datetime.datetime.today()
df_date_list = [df_base - datetime.timedelta(days=x) for x in range(0, 20)]
df = pd.DataFrame(df_date_list)
df.columns = ['day']
print(df)

# extract the week day name
df['day_of_week'] = df['day'].dt.day_name()
print(df.head())

# Engineer categorical variable by ordinal number replacement
weekday_map = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}
df['day_ordinal'] = df.day_of_week.map(weekday_map)
print(df.head(20))

# advantages of label encoding in ordinal categories
# 1)Keeps the semantical information of the variable (Human readable content)
# 2)Straightforward
