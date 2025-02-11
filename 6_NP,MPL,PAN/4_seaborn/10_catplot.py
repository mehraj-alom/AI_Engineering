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

# Create a categorical plot using seaborn's catplot function
# data=df: specifies the DataFrame to use for plotting
sns.catplot(data=df,  # specifies the DataFrame to use for plotting
            x="species",  # sets the x-axis variable to show different penguin species
            y="bill_length_mm",  # sets the y-axis variable to show bill length measurements
            hue="sex",  # splits each species by sex, using different colors
            kind="boxen",  # creates a boxen plot (enhanced box plot showing distribution)
            palette="pastel")  # sets the color scheme to pastel colors

# Display the plot
plt.show()