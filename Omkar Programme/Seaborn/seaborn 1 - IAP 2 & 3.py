# shift + tab for more information of any function in jupyter notebook
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# ===================== SEABORN LINE PLOT ========================

days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temperature = [36.6, 38, 39, 49, 29, 40.1, 40, 39, 30]
dataframe = pd.DataFrame({"days": days, "temperature": temperature})
# convert list of data into dataframes
sns.lineplot(x="days", y="temperature", data=dataframe)
# use columns of dataframe as x and y to plot lineplot in seaborn
plt.show()

tips_df = sns.load_dataset("tips")   # loaded dataset from github seaborn
print(tips_df)
print(tips_df.shape)       # to check rows and columns of dataset
sns.lineplot(x="total_bill", y="tip", data=tips_df)
plt.show()

sns.lineplot(x="size", y="total_bill", data=tips_df)
plt.show()

plt.figure(figsize=(16, 9))    # increase size of figure
sns.set(style="darkgrid")      # setting background of chart
sns.lineplot(x="size", y="total_bill", data=tips_df, hue="day",
             style="day", palette="winter", dashes=False,
             markers=["o", "<", ">", "^"], legend="brief")
# with x and y we can create a chart and hue show its values in that chart
# style changes style of line in lineplot chart
# with error values we can see what are correct values we can give to any parameter
# palette give chart in winter colors
# for remove dashes line do dashes=False
# marker show intersect point of x and y axis in various shape
# legend are graph information in small box and if it is False then it will hide
plt.title("Line Plot", fontsize=20)     # changing font size of chart title
plt.xlabel("Size", fontsize=15)
plt.ylabel("Total Bill", fontsize=15)
plt.show()
