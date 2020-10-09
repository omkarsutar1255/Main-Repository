# todo: Directing Customers to Subscription Through App Behavior Analysis

# todo: This is classification problem

# todo: Import essential libraries

import numpy as np  # for numeric calculation
import pandas as pd  # for data analysis and manupulation
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns  # for data visualization
from dateutil import parser  # convert time in date time data type

# todo: Import dataset & explore
fineTech_appData = pd.read_csv("FineTech_appData.csv")
print(fineTech_appData.shape)

# In[4]:


fineTech_appData.head(6)  # show fisrt 6 rows of fineTech_appData DataFrame  *****code 1

# In[5]:


fineTech_appData.tail(6)  # show last 6 rows of fineTech_appData DataFrame  *****code 2

# In[6]:


for i in [1, 2, 3, 4, 5]:
    print(fineTech_appData.loc[i, 'screen_list'], '\n')

# In[7]:


fineTech_appData.isnull().sum()  # take summation of null values

# In[8]:


fineTech_appData.info()  # brief inforamtion about Dataset

# In[9]:


fineTech_appData.describe()  # give the distribution of numerical variables  *****code 3

# In[10]:


# Get the unique value of each columns and it's length
features = fineTech_appData.columns
for i in features:
    print("""Unique value of {}\n{}\nlen is {} \n........................\n
          """.format(i, fineTech_appData[i].unique(), len(fineTech_appData[i].unique())))

# In[11]:


fineTech_appData.dtypes

# In[12]:


#  hour data convert string to int
fineTech_appData['hour'] = fineTech_appData.hour.str.slice(1, 3).astype(int)

# In[13]:


# get data type of each columns
fineTech_appData.dtypes

# In[14]:


fineTech_appData.columns

# In[15]:


# drop object dtype columns
fineTech_appData2 = fineTech_appData.drop(['user', 'first_open', 'screen_list', 'enrolled_date'], axis=1)

# In[16]:


fineTech_appData2.head(6)  # head of numeric dataFrame *****code 4

# # Data Visualization

# ## Heatmap Using Correlation matrix

# In[17]:


# Heatmap
plt.figure(figsize=(16, 9))  # heatmap size in ratio 16:9

sns.heatmap(fineTech_appData2.corr(), annot=True, cmap='coolwarm')  # show heatmap

plt.title("Heatmap using correlation matrix of fineTech_appData2", fontsize=25)  # title of heatmap *****code 5

# ## Pairplot of fineTech_appData2

# In[18]:


# Pailplot of fineTech_appData2 Dataset

# %matplotlib qt5 # for show graph in seperate window
sns.pairplot(fineTech_appData2, hue='enrolled')  # *****code 6

# ## Countplot of enrolled

# In[19]:


# Show counterplot of 'enrolled' feature
sns.countplot(fineTech_appData.enrolled)  # *****code 7

# In[20]:


# value enrolled and not enrolled customers
print("Not enrolled user = ", (fineTech_appData.enrolled < 1).sum(), "out of 50000")
print("Enrolled user = ", 50000 - (fineTech_appData.enrolled < 1).sum(), "out of 50000")

# ## Histogram of each feature of fineTech_appData2

# In[21]:


# plot histogram 

plt.figure(figsize=(16, 9))  # figure size in ratio 16:9
features = fineTech_appData2.columns  # list of columns name
for i, j in enumerate(features):
    plt.subplot(3, 3, i + 1)  # create subplot for histogram
    plt.title("Histogram of {}".format(j), fontsize=15)  # title of histogram

    bins = len(fineTech_appData2[j].unique())  # bins for histogram
    plt.hist(fineTech_appData2[j], bins=bins, rwidth=0.8, edgecolor="y", linewidth=2, )  # plot histogram

plt.subplots_adjust(hspace=0.5)  # space between horixontal axes (subplots) *****code 8

# In[22]:


for i, j in enumerate(features):
    print(i, j)

# ## Correlation barplot with 'enrolled' feature

# In[23]:


# show corelation barplot 

sns.set()  # set background dark grid
plt.figure(figsize=(14, 5))
plt.title("Correlation all features with 'enrolled' ", fontsize=20)
fineTech_appData3 = fineTech_appData2.drop(['enrolled'], axis=1)  # drop 'enrolled' feature
ax = sns.barplot(fineTech_appData3.columns, fineTech_appData3.corrwith(fineTech_appData2.enrolled))  # plot barplot
ax.tick_params(labelsize=15, labelrotation=20, color="k")  # decorate x & y ticks font *****code 9

# In[24]:


# parsing object data into data time format

fineTech_appData['first_open'] = [parser.parse(i) for i in fineTech_appData['first_open']]

# In[25]:


fineTech_appData['enrolled_date'] = [parser.parse(i) if isinstance(i, str) else i for i in
                                     fineTech_appData['enrolled_date']]

# In[26]:


fineTech_appData.dtypes

# In[27]:


fineTech_appData['time_to_enrolled'] = (fineTech_appData.enrolled_date - fineTech_appData.first_open).astype(
    'timedelta64[h]')

# In[28]:


# plot histogram
plt.hist(fineTech_appData['time_to_enrolled'].dropna())  # *****code 10

# In[29]:


# Plot histogram
plt.hist(fineTech_appData['time_to_enrolled'].dropna(), range=(0, 100))  # *****code 11

# In[30]:


# Those customers have enrolled after 48 hours set as 0
fineTech_appData.loc[fineTech_appData.time_to_enrolled > 48, 'enrolled'] = 0

# In[31]:


fineTech_appData

# In[32]:


fineTech_appData.drop(columns=['time_to_enrolled', 'enrolled_date', 'first_open'], inplace=True)

# In[33]:


fineTech_appData

# In[34]:


# read csv file and convert it into numpy array
fineTech_app_screen_Data = pd.read_csv("Dataset/FineTech appData/top_screens.csv").top_screens.values

# In[35]:


fineTech_app_screen_Data

# In[36]:


type(fineTech_app_screen_Data)

# In[37]:


# Add ',' at the end of each string of  'sreen_list' for further operation.
fineTech_appData['screen_list'] = fineTech_appData.screen_list.astype(str) + ','

# In[38]:


fineTech_appData

# In[39]:


# string into to number

for screen_name in fineTech_app_screen_Data:
    fineTech_appData[screen_name] = fineTech_appData.screen_list.str.contains(screen_name).astype(int)
    fineTech_appData['screen_list'] = fineTech_appData.screen_list.str.replace(screen_name + ",", "")

# In[40]:


# test
fineTech_appData.screen_list.str.contains('Splash').astype(int)

# In[41]:


# test
fineTech_appData.screen_list.str.replace('Splash' + ",", "")

# In[42]:


# get shape
fineTech_appData.shape

# In[43]:


# head of DataFrame
fineTech_appData.head(6)  # *****code 12

# In[44]:


# remain screen in 'screen_list'
fineTech_appData.loc[0, 'screen_list']

# In[45]:


fineTech_appData.screen_list.str.count(",").head(6)

# In[46]:


# count remain screen list and store counted number in 'remain_screen_list'

fineTech_appData['remain_screen_list'] = fineTech_appData.screen_list.str.count(",")

# In[47]:


# Drop the 'screen_list'
fineTech_appData.drop(columns=['screen_list'], inplace=True)

# In[48]:


fineTech_appData

# In[49]:


# total columns
fineTech_appData.columns

# In[50]:


# take sum of all saving screen in one place
saving_screens = ['Saving1',
                  'Saving2',
                  'Saving2Amount',
                  'Saving4',
                  'Saving5',
                  'Saving6',
                  'Saving7',
                  'Saving8',
                  'Saving9',
                  'Saving10',
                  ]
fineTech_appData['saving_screens_count'] = fineTech_appData[saving_screens].sum(axis=1)
fineTech_appData.drop(columns=saving_screens, inplace=True)

# In[51]:


fineTech_appData

# In[52]:


credit_screens = ['Credit1',
                  'Credit2',
                  'Credit3',
                  'Credit3Container',
                  'Credit3Dashboard',
                  ]
fineTech_appData['credit_screens_count'] = fineTech_appData[credit_screens].sum(axis=1)
fineTech_appData.drop(columns=credit_screens, axis=1, inplace=True)

# In[53]:


fineTech_appData

# In[54]:


cc_screens = ['CC1',
              'CC1Category',
              'CC3',
              ]
fineTech_appData['cc_screens_count'] = fineTech_appData[cc_screens].sum(axis=1)
fineTech_appData.drop(columns=cc_screens, inplace=True)

# In[55]:


fineTech_appData

# In[56]:


# End ==================================================<br>
# This Project Created By www.IndianAIProduction.com<br>
# Project Source: www.IndianAIProduction.com/directing-customers-to-subscription-through-financial-app-behavior-analysis-ml-project<br>
# ML Projects: www.IndianAIProduction.com/machine-learning-projects<br>
# Videos: www.YouTube.com/IndianAIProduction
