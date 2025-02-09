import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns 
import numpy as np 

df = sns.load_dataset("penguins").head(160)
print(df)
# Fill missing values
df["sex"] = df["sex"].fillna(np.random.choice(["Male", "Female"]))
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(np.random.randint(13, 22))  # Adjusted to match data range
df["body_mass_g"] = df["body_mass_g"].fillna(np.random.randint(3000, 6000))

#Plotting Scatterplot
sns.scatterplot(data=df,
                x="bill_depth_mm",
                y="body_mass_g",
                hue="sex",
                style="species",
                size="island",
                sizes=(50, 200),  # Increased size range for better visibility
                palette="icefire_r",
                # alpha=0.6,  # Uncommented alpha for better visibility
                markers={"Adelie": "o", "Chinstrap": ">", "Gentoo": "s"},
                # sizes=(50, 400,)  # Increased size range for better visibility
                )  # Corrected markers for species
plt.show()