import pandas as pd
import seaborn as sns 
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/train.csv").head(40)
df = df.set_index("Row ID")
print(df)
df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.month
# Convert 'State' to a numeric variable
# df['State'] = df['State'].astype('category').cat.codes
sns.set(style="darkgrid")
plt.grid(True)
sns.barplot(x="Ship Mode", y="Order Date", data=df, order=["First Class","Second Class","Standard Class"],
            hue="Region", hue_order=["South", "East", "West", "Central"], errorbar="sd", errcolor="g", errwidth=2,
            ci=12, orient="v", color="y", saturation=0.4,alpha=0.7)
plt.show()

#We cannot plot bargraph horizontally if the x or y axis containing non numerical data