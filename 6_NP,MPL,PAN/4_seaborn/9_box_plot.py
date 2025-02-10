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

sns.set_style("whitegrid")
sns.boxplot(x="island", y="bill_length_mm", data=df,hue="sex",palette="Set2",showmeans=True)
plt.show()

#plot a box plot for single variable
sns.boxplot(x=df["bill_length_mm"],showmeans=True)
plt.show()