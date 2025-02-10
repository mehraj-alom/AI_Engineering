import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
print(df)
# Fill missing values
df["sex"] = df["sex"].fillna(np.random.choice(["Male", "Female"]))
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(np.random.randint(13, 22))  # Adjusted to match data range
df["body_mass_g"] = df["body_mass_g"].fillna(np.random.randint(3000, 6000))
print(df)

sns.stripplot(x="species",           # x-axis categorical variable
              y="bill_length_mm",      # y-axis numerical variable
              data=df,                 # dataframe containing the data
              palette="Set2",          # color palette for the plot
              hue="sex",              # variable for color differentiation
              jitter=True,            # adds random noise to prevent overlapping points
              size=4,                 # size of the markers
              marker=">",             # shape of the markers
              alpha=0.7)              # transparency of the markers (0 to 1)
plt.show()

# TO make a stripplot of a single variable
sns.stripplot(x=df["bill_length_mm"], # single numerical variable for distribution
              palette="Set2")          # color palette for the plot
plt.show()