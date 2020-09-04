import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()
# print(cancer_dataset)
cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'], cancer_dataset['target']],
                         columns=np.append(cancer_dataset['feature_names'], ['target']))
# print(cancer_df)
sns.pairplot(cancer_df, hue='target', hue_order=[1.0, 0.0], palette='winter',
             vars=['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness'], x_vars=None, y_vars=None,
             kind="scatter", diag_kind="hist", markers=['*', '<'],
             height=1, aspect=1, corner=False, dropna=True,
             plot_kws=None, diag_kws=None, grid_kws=None, size=None)
# pairplot - it take each adjacent columns from dataframe as x & y and plot any kind of graph for every x & y axis
# vars - we can show pairplot for limited columns of dataframe by mension columns names in var parameter
# hue - it take column name and that column values assigned with various color
#       so that in graph we can separate that values by their color
# hue order - it takes values to assign different color to it
# palette - it take type of colors we want for graph
# x_var and y_var - it takes x and y variable for plotting every graph
# kind - it takes scatter or regular plotting method for graph
# diag_kind - it takes graph method for show that kind graph at diagonal
# marker - we can give shape to points so we can check separated points on graph
# height - it enables us to change size of each graph

plt.show()
