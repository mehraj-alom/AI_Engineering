import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/2_Disease_detectionsystem/heart_disease_uci.csv")
print(df.head(20))
df = df.head(40)
sns.scatterplot(
    x="age",
    y="thalch",
    data=df,
    hue="sex",
    palette="Set1",
    alpha=0.7,
    edgecolor="black",
    linewidth=1
)
# sns.countplot(x="sex", 
#               data=df,
#               hue="sex",
#               palette="Set1",
#               alpha=0.7,
#               edgecolor="black"
#             )
plt.show()