import matplotlib.pyplot as plt

x = [1, 5, 4]
y = [23, 45, 89]
plt.plot(x, y)

plt.axis([0, 10, 0, 100])  # x-axis = 0-30 and y-axis = 0-50
# we can set length of x and y axis in graph
plt.title("omkar's graph", fontsize=15)   # increase size of title
plt.xlabel("temp", fontsize=15)      # we can set fontsize to xlabel
plt.ylabel("days", fontsize=15)      # also for ylabel set fontsize
plt.legend(['single element'], loc=2)   # line name and location is mention in graph
plt.grid(color="k", linestyle="-.", linewidth=1)  # we can create various background grids
plt.show()

import numpy as np
std_age = np.random.randint(18, 45, (100))
tea_age = np.random.randint(15, 40, (100))
print(std_age)
print(tea_age)

classes = ["python", "R", "c language", "c++"]
class1 = np.random.randint(10, 40, 4)
print(class1)
plt.bar(classes, class1, width=0.4, align="edge", color="y", edgecolor="m", linewidth=5, linestyle="--", alpha=0.5,
         label="class 1")
# width specify widthsize of bar, align bar at edge or center, color of bar,
# edgecolor are color at bar edge, linewidth is edge line size, linestyle is edgeline style,
# alpha is darkness of bar, label are label for bar chart
plt.show()

import pandas as pd
df_google = pd.read_csv("F:\Omkar\googleplaystore.csv", nrows=1000)  # to retrieve only 1000 rows from dataset
# print(df_google.shape)
x = df_google["Rating"]
y = df_google["Reviews"]
plt.scatter(x, y, c="r", marker="*", s=10, alpha=0.3, linewidths=7, edgecolors="g") # we can give color of scatter point
# marker gives shape of points and s is used to set size of pointer, aplpha set darkness and faintness of points
# we can set linewidth of marker edge, we can set edgecolor
plt.show()

classses = ["a", "b", "c", "d", "e"]
class1 = [45, 65, 71, 55, 66]
# plt.pie([1])
plt.pie(class1, labels=classses, autopct="%0.1f%%", pctdistance=0.7, labeldistance=1.2, counterclock=False,
        wedgeprops={"linewidth":2, "width":1, "edgecolor":"k"}, center=(2, 3), rotatelabels=True)
# we can give distance to percentage and labels from center, we can set direction to pie chart
# we can set center position of pie chart, we can set rotate label to pie chart
# in wedge properties linewidth is broadness of edgeline and width is distance of edge from center
# edge color is the color we can give to edge to pie chart
plt.legend()        # legend gives basic information of graph
plt.show()

plt.figure(figsize=(7, 4))
colors = ["r", "w", "r", "w", "r", "w", "r", "w", "r", "w", "r", "w", "r", "w"]
labels = [np.ones(14)]
plt.pie([1], colors="k", radius=1.5)
plt.pie(labels, colors=colors, radius=1.4)
plt.pie([1], colors="g", radius=1.1)
plt.pie([1], colors="y", radius=1.0)
plt.pie([1], colors="c", radius=0.9)
plt.pie([1], colors="b", radius=0.8)
plt.pie([1], colors="m", radius=0.7)
plt.pie([1], colors="b", radius=0.6)
plt.pie(labels, colors=colors, radius=0.5)
plt.pie([1], colors="w", radius=0.3)
plt.pie([1], colors="k", radius=0.15)
plt.show()
# this is how we can create various pie charts

# ===========CREATING VARIOUS GRAPHS IN ONE CHART==============
plt.subplot(3, 2, 1)   # 3 rows and 2 columns means we can put 3*2=6 graphs in one chart
plt.plot([12, 23, 24], [11, 22, 33])                 # we can put line plot
plt.subplot(3, 2, 2)
plt.hist([1, 2, 3])              # we can put histogram
plt.subplot(3, 2, 3)
plt.bar([1, 2, 3], [1, 2, 1])           # we can put bar graph
plt.subplot(3, 2, 4)
plt.scatter([1, 2, 3, 4], [1, 2, 3, 1])        # we can put scatter plot
plt.subplot(3, 2, 5)
plt.pie([1, 2, 3, 4, 5])     # we can put pie chart
plt.subplot(3, 2, 6, projection="polar", facecolor="k", frameon=False)    # we can put polar graph
plt.show()

import matplotlib.image as mpimg
img = mpimg.imread("F:\\aditya\IMG_1586.JPG")  # read image in png format
# print(img)
print(type(img))
print(img.shape)
print(img.ndim)
single_channel = img[:, :, 1]   # converting image in single channel
plt.figure(figsize=(9, 6))
plt.axis("off")          # its don't display axis on chart
# plt.imshow(img, cmap='winter')       # cmap gives color bar in many type in chart
plt.imshow(single_channel, cmap='RdGy')   # single channel with cmap convert image to any colors combination
plt.colorbar()           # shows color bar of colors that are used in chart
plt.show()               # display image

cmap = """Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges',
'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r',
'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r',
'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r',
'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r',
'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r',
'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r',
'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray',
'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern',
'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot',
'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic',
'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r',
'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r',
'viridis', 'viridis_r', 'winter', 'winter_r"""

# we can use multiple cmap types on any photos
single_channel2_img = img[:,:,1]
cmap_name_list = cmap.split(sep="', '")
print(cmap_name_list)
save_image_addr_name = []
for i in range(len(cmap_name_list)):
    cmap_str = cmap_name_list[i]
    save_image_addr_name.append("F:\Omkar\matplotlib"+ cmap_name_list[i] + ".png")
for i in range(len(cmap_name_list)):
    cmap_name = cmap_name_list[i]
    plt.imshow(single_channel2_img, cmap=cmap_name)
    plt.savefig(save_image_addr_name[i], orientation='portrate', facecolor="k")
    plt.show()

