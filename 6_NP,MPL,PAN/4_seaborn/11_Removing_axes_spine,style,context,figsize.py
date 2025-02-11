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

plt.figure(figsize=(3, 4))  # Set the figure size
sns.set_style("whitegrid")  # Set the style to whitegrid for a clean look
sns.set_context("paper",font_scale=2)  
sns.barplot(x="species", y="bill_length_mm", data=df)
sns.despine()  # Remove the top and right spines from the plot for a cleaner look
# sns.despine(left=True)  # Optional: Can also remove left spine by setting left=True
plt.show()  # Display the plot