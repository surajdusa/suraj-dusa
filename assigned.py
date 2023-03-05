import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rc('figure', figsize=(20, 10))


# this functions converts our csv file to a usable dataframe and assert it is
# with isinstance


def csv_to_dataframe(str):
    """this functions converts our csv file to a usable dataframe and assert it is with isinstance"""
    global df
    df=pd.read_csv(str)
    print(isinstance(df,pd.DataFrame))
#string passed is the location of the csv file to be converted into a dataframe in this case its in the same dir
csv_to_dataframe("clean_dataset.csv")


#print the dataframe head first five rows
df.head()

#print the summary statistics mean variance and other central tendecy stats
df.describe()

def multi_line_data():
    """obtaining y data (debt) for multiline plot where will be plotting various industries against credit approval"""
    k=df["Industry"].unique()
    #print(k)
    lister=[]
    for x in range(0,(len(k))):
         lister.append(df["Debt"].where(df.Industry==k[x]).fillna(0).to_numpy())
    return lister
#multi_line_data()
# multiline plot for debt according to industry

#our multiline plot 

plty=multi_line_data()
ref=df["Industry"].unique()
mui=0
print(len(plty[0]))
while mui < (len(ref)):
   plt.plot([x for x in range(0,690)], plty[mui], label=ref[mui] )
   mui+=1


plt.legend()
plt.xlabel('people')
plt.ylabel("debt")
plt.title('debt vs industry worked in')

# show the plot
plt.show()


# a donut chart showing sums cred approval rates debt....all compared to each other overtime 

"""  a donut chart showing sums cred approval rates debt....all compared to each other over time overtime """
labels = list(ref.tolist())
sizes = [np.sum(x) for x in plty]
colors=['greenyellow', 'deeppink', 'indianred', 'lightgrey', 'orchid', 'lavender', 'mediumseagreen', 'magenta', 'darkslateblue', 'chartreuse', 'gold', 'teal', 'whitesmoke', 'lightsalmon']

# create the outer and inner circles
outer_circle = plt.Circle((0,0), 0.7, color='white')
inner_circle = plt.Circle((0,0), 0.4, color='white')

# create the donut chart using pie()
plt.pie(sizes, labels=labels, colors=colors, wedgeprops=dict(width=0.3), startangle=90)

# add the circles to create the donut shape
plt.gcf().gca().add_artist(outer_circle)
plt.gcf().gca().add_artist(inner_circle)

# add a title
plt.title('sum of debt according to the industry')

# show the plot
plt.show()


# 3d surface map** for sine of(Σ(income,debt))

# this is the graph of the sine of central variance showing instead of standard variance derive from the sum of income and debt


""" this is the graph of the sine of central variance showing instead of standard variance derive from the sum of income and debt"""
from matplotlib import cm
from matplotlib.ticker import LinearLocator
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# Make data.
X=df.Debt.values
Y=df.Income.values
X, Y = np.meshgrid(X, Y)
K=X+Y
Z = np.sin((K-np.mean(K)))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# generate colors for pie chart if you want to cusomize

import random
import matplotlib.colors as mcolors

# get a list of all named colors in matplotlib
all_colors = list(mcolors.CSS4_COLORS.keys())

# randomly select fourteen colors from the list
random_colors = random.sample(all_colors, 14)

# print the list of random colors
print(random_colors)

