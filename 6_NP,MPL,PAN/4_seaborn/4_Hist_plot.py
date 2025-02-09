import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Load dataset
df = sns.load_dataset("penguins")

# Fill missing values
df["sex"] = df["sex"].fillna(np.random.choice(["Male", "Female"]))
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(np.random.randint(13, 22))  # Adjusted to match data range
df["body_mass_g"] = df["body_mass_g"].fillna(np.random.randint(3000, 6000))

# Define bins based on data range (13.1–21.5 mm)
bins = np.arange(13, 22.5, 1)  # Bins: 13,14,15,...,21,22 (covers 13.1–21.5)

# Create the plot
sns.displot(
    df,
    x="bill_depth_mm",
    hue="sex",
    bins=bins,
    palette={"Male": "blue", "Female": "pink"},  # Distinct colors
    alpha=0.6,  # Transparency for overlapping bars
    kde=True,  # Disable KDE for clarity
    edgecolor="black",  # Add bar borders
    linewidth=0.5,
    # log_scale=True
    
    
)

# Customize labels and title
plt.title("Distribution of Bill Depth by Sex (Adjusted Bins)", fontsize=14)
plt.xlabel("Bill Depth (mm)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(bins)  # Explicitly show all bin edges
plt.grid(axis="y", linestyle="--", alpha=0.5)  # Add gridlines for readability
plt.show()
