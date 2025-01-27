import pandas as pd
import numpy as np
# The crosstab function in pandas is used to compute a simple cross-tabulation of two (or more) 
# factors. It is essentially a pivot table that summarizes the relationship between two categorical
# variables. The result is a DataFrame that shows the frequency (or other aggregation) of the
# combinations of the specified factor
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack', 'Karen', 'Leo', 'Mona', 'Nina', 'Oscar'],
    'nationality': ['USA', 'Canada', 'UK', 'Germany', 'USA', 'Canada', 'UK', 'Germany', 'USA', 'Canada', 'UK', 'Germany', 'USA', 'Canada', 'UK'],
    'sex': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'M'],
    'age': [25, 30, 35, 40, 22, 28, 32, 27, 29, 31, 26, 34, 33, 24, 25],
    'handedness': ['Right', 'Left', 'Right', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left']
}
# Adding more data with similar nationality, age, and sex
data['name'].extend(['Paul', 'Quincy', 'Rachel', 'Steve', 'Tina'])
data['nationality'].extend(['USA', 'Canada', 'UK', 'Germany', 'USA'])
data['sex'].extend(['M', 'M', 'F', 'M', 'F'])
data['age'].extend([25, 30, 35, 40, 22])
data['handedness'].extend(['Right', 'Left', 'Right', 'Right', 'Left'])
df = pd.DataFrame(data)
print(df)
df1 = pd.crosstab(df["nationality"],df["handedness"],margins=True)
print("2__\n",df1,"\n")
df2 = pd.crosstab(df["sex"],df["handedness"],margins=True)
print("3__\n",df2,"\n")
df3 = pd.crosstab(df["sex"],[df["nationality"],df["age"]],margins=True,rownames=["SEX"],colnames=["Country","old"])
print("3__\n",df3,"\n")
df4 = pd.crosstab(df['sex'],df['handedness'],normalize=True,margins=True,margins_name="Percentage",values=df["age"],aggfunc="mean")
print("4__\n",df4,"\n")
df5 = pd.crosstab(df['sex'],df['handedness'],values=df["age"],aggfunc="mean")
print("4__\n",df5,"\n")
df6 = pd.crosstab(df['sex'],df['handedness'],values=df["age"],aggfunc=np.average)
print("4__\n",df6,"\n")