# ============= SEABORN SCATTERPLOT ==============
import seaborn as sns
import matplotlib.pyplot as plt
tatanic_df = sns.load_dataset("titanic")
plt.figure(figsize=(16, 9))
sns.scatterplot(x='age', y='fare', hue='sex', style='who', size='who', data=tatanic_df,
                palette='winter', hue_order=None, hue_norm=None,
                sizes=(40, 200), size_order=None, size_norm=None,
                markers=True, style_order=None,
                x_bins=None, y_bins=None,
                units=None, estimator=None, ci=95, n_boot=1000,
                alpha=0.7, x_jitter=None, y_jitter=None,
                legend="brief", ax=None)
# x and y = it takes parameters for x and y axis on graph
# hue = it gives different color for elements to show which is male and which is female point according to sex column
# style = it gives different shapes for elements to show which is elder, younger and child according to who column
# sizes = it takes min and max values for size for shape of style
plt.show()

plt.figure(figsize=(16, 9))
sns.scatterplot(x='age', y='fare', data=tatanic_df)
sns.lineplot(x='age', y='fare', data=tatanic_df)
sns.barplot(x='age', y='fare', data=tatanic_df)
plt.show()
