# todo: import library
import pandas as pd

# todo: load dataset
df = pd.read_csv("heights.csv")
df.head()

# todo:Detect outliers using percentile
max_thresold = df['height'].quantile(0.95)
print(max_thresold)
print(df[df['height'] > max_thresold])
min_thresold = df['height'].quantile(0.05)
print(min_thresold)
print(df[df['height'] < min_thresold])

# todo: Remove outliers
print(df[(df['height'] < max_thresold) & (df['height'] > min_thresold)])

# todo: Now lets explore banglore property prices dataset
df = pd.read_csv("bhp.csv")
df.head()
print(df.shape)
df.describe()

# todo: Explore samples that are above 99.90% percentile and below 1% percentile rank
min_thresold, max_thresold = df.price_per_sqft.quantile([0.001, 0.999])
print(min_thresold, max_thresold)
print(df[df.price_per_sqft < min_thresold])
print(df[df.price_per_sqft > max_thresold])

# todo: Remove outliers
df2 = df[(df.price_per_sqft < max_thresold) & (df.price_per_sqft > min_thresold)]
print(df2.shape)
df2.describe()
