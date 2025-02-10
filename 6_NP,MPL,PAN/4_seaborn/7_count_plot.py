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
# Create a count plot using seaborn
# data: specifies the DataFrame to use
# x: specifies the column to plot on x-axis
# hue: creates separate colored bars based on species column
# palette: defines color scheme ("Set2" is a predefined color palette)
# dodge: if True (default), bars will be placed side by side
# order: can specify custom order of x-axis categories
# saturation: controls color intensity (0-1)
sns.countplot(data=df, 
              x="sex",
              hue="species",
              palette="Set2",
              dodge=True,
              saturation=0.8,
              order=["Male", "Female"])

# Display the plot
plt.show()