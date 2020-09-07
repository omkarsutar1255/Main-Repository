# %matplotlib inline                  # This is used for jupiter notebook for show charts on screen
from matplotlib import pyplot as plt
plt.plot([1, 3, 6], [1, 3, 8])        # create chart with elements in plt.plot
plt.plot([1, 3, 6], [1, 4, 7])        # create second plot in same chart to compare
plt.title("omkar's data")             # giving title to chart
plt.xlabel("X values")                # giving label to x-axis
plt.ylabel("Y values")                # giving label to y-axis
plt.show()                            # show the created plot


from matplotlib import style
style.use("ggplot")         # styles for background of chart(use at multiple charts)
x = [1, 5, 4]
y = [23, 45, 89]
x2 = [3, 7, 3]
y2 = [5, 8, 9]
plt.plot(x, y, label="first", linewidth=6)                       # putting x and y values for plot
plt.plot(x2, y2, label="second", linewidth=3)                     # putting x2 and y2 values for new plot
# linewidth enables to change width of line in chart
plt.legend(loc="best", shadow=True, fontsize="large")               # its show labels information in chart
# location of legend can be changed (by default its best means it find best place to locate in chart
# shadow property will give shadow designed legend
# we can provide size of words of legend using fontsize
plt.show()                           # showing 2 plots in same chart for comparision
# we can use plt.scatter to plot values in scatter format
# we can use plt.hist to plot values in histogram format
