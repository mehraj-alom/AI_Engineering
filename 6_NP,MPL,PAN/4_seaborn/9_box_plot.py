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

# Set the style of the plot to whitegrid
sns.set_style("whitegrid")  # Set the visual style of the plot to use white background with grid lines

# Create a box plot comparing bill length across islands, separated by sex
sns.boxplot(
    x="island",           # Specify the column for x-axis categories (different islands)
    y="bill_length_mm",   # Specify the column for y-axis numerical values (bill length measurements)
    data=df,             # Specify the DataFrame containing the data
    hue="sex",           # Create separate boxes for each sex within each island category
    palette="Set2",      # Set the color scheme for the boxes using Set2 color palette
    showmeans=True       # Show mean values as markers in addition to median lines
)
plt.show()              # Display the plot
# Create a box plot for single variable (bill length)
sns.boxplot(x=df["bill_length_mm"],showmeans=True)
plt.show()