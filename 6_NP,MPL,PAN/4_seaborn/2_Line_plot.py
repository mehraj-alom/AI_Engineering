import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/train.csv").head(40)

# Convert 'Order Date' to datetime and extract the year
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y').dt.year

# Drop duplicates based on 'Order Date'
unique_years_df = df.drop_duplicates(subset='Order Date')

# Print the first 10 rows of the unique years DataFrame
print(unique_years_df.head(10))

# Plotting a line plot (example with numerical data)
# Assuming you want to plot 'Order Date' against some numerical column, e.g., 'Sales'
unique_countries = df['Country'].unique()
sns.lineplot(x="Order Date", y="Sales", data=df, hue="Ship Mode", style="Ship Mode", palette="magma", markers=["o",">"],
             dashes=False, legend=False)
plt.title("Sales Seaborn Chart")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.grid(True)
# Show the plot
plt.show()