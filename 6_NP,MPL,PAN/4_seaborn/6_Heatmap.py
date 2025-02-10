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
# Calculate correlations between all numerical columns and store in a matrix
correlation_matrix = df.corr()
new_df = df.drop(columns=['species', 'island', 'sex']).head(20)

# Create a new figure window with specified size
plt.figure(figsize=(10, 8))    # 10 inches width, 8 inches height

# Create heatmap using seaborn
sns.heatmap(
    new_df,        # Input data: matrix of correlation values
    annot=True,               # Show numerical values in each cell
    annot_kws={"color":"w","fontsize":8},  # Font size,color for annotations
    linecolor= "black",      # Color of the lines separating cells
    linewidths=1,           # Width of the lines separating cells
    # square=True,              # Make the cells square
    # cbar=False,               # Hide the colorbar
    # cbar_kws={"shrink": 0.75},  # Adjust the size of the colorbar
    cmap='coolwarm',          # Color scheme: red for positive, blue for negative correlations                 
    center=0,                  # Center the colormap at value 0
    vmin = 1,                # Minimum value for the colormap scale
    vmax= 90,                # Maximum value for the colormap scale 
    # xticklabels=False,      # Hide x-axis tick labels
    # yticklabels=False,      # Hide y-axis tick labels
)

# Add a title to the plot
plt.title('Correlation Heatmap of Penguin Features')

# Display the final visualization
plt.show()