from matplotlib import pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 53, 58, 34, 78, 57, 67]
plt.plot(x, y, color="green", linestyle="dashdot")
# we can give color and linestyle to lines of chart
plt.show()

x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 53, 58, 34, 78, 57, 67]
plt.plot(x, y, marker="D", linestyle="", markersize=10, alpha=0.5)  # marker are shape created at intersect point of x,y
# we can give marker, linestyle and color values in string character
# we can give markersize to change in sizes of marker
# alpha is used to make line faint or dark
plt.plot(x, y, "g+-.")
# we can directly mention marker, linestyle, color values
plt.show()

days = [1, 2, 3, 4, 5]
min_t = [40, 41, 39, 42, 38]
max_t = [50, 51, 49, 52, 48]
avg = [45, 46, 44, 47, 43]
plt.plot(days, min_t)
plt.plot(days, max_t)
plt.plot(days, avg)
plt.grid()               # grid show matching background with points in chart
plt.show()               # many plots with various info in one chart

company = ["google", "amz", "face", "apl"]
revenue = [100, 130, 70, 90]
profit = [20, 30, 20, 10]
xpos = np.arange(len(company))       # gives 0,1,2,3 for plot
plt.xticks(xpos, company, rotation=20)          # replacing xpos values with company values from chart
# rotation used to rotate company names from chart for certain degree
plt.bar(xpos-0.2, revenue, width=0.4)               # resenting bar with xpos and revenue
plt.bar(xpos+0.2, profit, width=0.4)                # width will set width of bar and shift their position with 0.2
plt.show()
# we can provide barh for horizontal bars

blood_suger = [113, 85, 90, 150, 149, 88, 93, 115, 80, 77, 82, 129]
plt.hist(blood_suger, bins=5, rwidth=0.90)             # bins takess no. of bars and rwidth takes space between two bars
plt.show()
plt.hist(blood_suger, bins=[75, 90, 105, 120, 135, 150], rwidth=0.90, color="g", histtype="step")
# we can provide bar width and color and style of bars with histtype
plt.show()
men_BP = [113, 85, 90, 150, 149, 88, 93, 115, 80, 77, 82, 129]
women_BP = [110, 80, 95, 145, 145, 85, 90, 110, 75, 75, 80, 125]
plt.figure(figsize=(16, 9))                              # it can use for various charts
plt.hist([men_BP, women_BP], bins=12, rwidth=0.90, color=["g", "b"], label=["men", "women"], orientation="horizontal")
# orientation shows vertical or horizontal histogram
plt.legend()

plt.show()

prices = [5, 10, 7, 20, 12]
foods = ["chapati", "roti", "rice", "paneer", "cury"]
plt.axis("equal")                  # gives pie chart in round shape
# plt.pie(prices, labels=foods)        # pie chart takes values with labels
plt.pie(prices, labels=foods, radius=1.5, autopct="%0.2f%%", explode=[0.07, 0, 0.1, 0, 0],
        startangle=90, colors=["c", "b", "r", "y", "g"], shadow=True, textprops={"fontsize":15})
# we can change size of pie circle and autopct show percentage upto given decimal point
# explode will extract piece of pie with some distance and startangle takes starting angle of first piece of pie
# we can give manual colors to pie chart and shadow gives shadow look to pie chart
# we can fontsize to text of pie chart
plt.show()

plt.savefig("piechart2.png", bbox_inches="tight", pad_inches=2, transparent=True)
# plt.savefig will save empty fig if chart is shown (plt.show())
# to save file specify name of file
# bbox fits chart in limited spece
# pad give extra scape around chart
# transparent gives chart without background
# we can save chart in any format.
# we can set resolution of chart fig using dpi feature
# we can set background color of chart using facecolor feature

