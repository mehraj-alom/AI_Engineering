import pandas as pd
data = {
    'Country': ['USA', 'USA', 'Canada', 'Canada'],
    'State': ['California', 'California', 'Ontario', 'Ontario'],
    'City': ['Los Angeles', 'San Francisco', 'Toronto', 'Ottawa'],
    'Population': [4000000, 870000, 2731571, 934243]
}

df = pd.DataFrame(data)
print("Real-life DataFrame:\n", df, "\n")

# Set the index to columns Country, State, and City
df1 = df.set_index(['City']).stack()

print("Stacked DataFrame:\n", df1)

df2 = df1.unstack(level=0)
print("Unstacked DataFrame:\n", df2)
# The stack method in pandas is used to pivot the columns of a DataFrame into the index,
# producing a Series with a multi-level index. This is useful for reshaping data, especially
# when you want to convert a wide DataFrame into a long format.