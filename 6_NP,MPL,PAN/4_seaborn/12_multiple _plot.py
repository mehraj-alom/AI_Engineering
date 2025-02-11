import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load the penguins dataset from seaborn
df = sns.load_dataset("penguins")
print(df)

# Fill missing values in the dataset
# Randomly fill missing sex values with Male or Female
df["sex"] = df["sex"].fillna(np.random.choice(["Male", "Female"]))
# Fill missing bill depth values with random numbers between 13-22mm
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(np.random.randint(13, 22))  # Adjusted to match data range
# Fill missing body mass values with random numbers between 3000-6000g
df["body_mass_g"] = df["body_mass_g"].fillna(np.random.randint(3000, 6000))
print(df)

fg = sns.FacetGrid(df, col="sex",
                   hue="species", 
                   height=4, 
                   aspect=1.5, 
                   palette="Set1")
fg.map(plt.scatter, "bill_length_mm", "bill_depth_mm").add_legend()
plt.show()