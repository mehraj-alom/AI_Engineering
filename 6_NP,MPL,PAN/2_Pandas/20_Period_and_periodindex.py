import pandas as pd
import numpy as np
# Create a yearly period object
y = pd.Period('2016')
print(type(y))  # Output the type of the period object
print(y)  # Output the period object
# print(dir(y))  # Uncomment to see all attributes and methods of the period object
print(y.start_time)  # Output the start time of the period
print(y.end_time)  # Output the end time of the period

# Create a monthly period object
m = pd.Period("2026-1", freq="M")
print(m)  # Output the monthly period object
print(m.start_time)  # Output the start time of the monthly period
print(m.end_time)  # Output the end time of the monthly period

# Add 1 month to the monthly period object and output the result
print("3__\n", m + 1, "\n")

# Create a daily period object
d = pd.Period("2016", freq="D")
print("4__\n", d)  # Output the daily period object
print(d.start_time)  # Output the start time of the daily period
print(d.end_time)  # Output the end time of the daily period
print(d + 10, "\n")  # Add 10 days to the daily period object and output the result

# Create a quarterly period object
Q = pd.Period("2025Q1", freq="Q")
print("4__\n", Q)  # Output the quarterly period object
print(Q.start_time)  # Output the start time of the quarterly period
print(Q.end_time)  # Output the end time of the quarterly period
print(Q + 4, "\n")  # Add 4 quarters to the quarterly period object and output the result

# Create a quarterly period object with fiscal year ending in February
Q = pd.Period("2025Q1", freq="Q-FEB")
print("5__\n", Q)  # Output the quarterly period object with fiscal year ending in February
print(Q.start_time)  # Output the start time of the quarterly period
print(Q.end_time)  # Output the end time of the quarterly period
print(Q - 1, "\n")  # Subtract 1 quarter from the quarterly period object and output the result


# Arithmetic operations on periods

# Create a weekly period object
w = pd.Period("2023-10-01", freq="W")
print("Weekly period object:\n", w)  # Output the weekly period object
print(w.start_time)  # Output the start time of the weekly period
print(w.end_time)  # Output the end time of the weekly period
print(w + 2, "\n")  # Add 2 weeks to the weekly period object and output the result

# Create an hourly period object
h = pd.Period("2023-10-01 05:00", freq="H")
print("Hourly period object:\n", h)  # Output the hourly period object
print(h.start_time)  # Output the start time of the hourly period
print(h.end_time)  # Output the end time of the hourly period
print(h - 5, "\n")  # Subtract 5 hours from the hourly period object and output the result

# Create a minute period object
min_p = pd.Period("2023-10-01 05:30", freq="T")
print("Minute period object:\n", min_p)  # Output the minute period object
print(min_p.start_time)  # Output the start time of the minute period
print(min_p.end_time)  # Output the end time of the minute period
print(min_p + 15, "\n")  # Add 15 minutes to the minute period object and output the result



# PERIOD INDEX 
p = pd.period_range(start="2025",periods=10,freq="Q")
print("6__\n",p,"\n")
ps = pd.Series(np.random.rand(len(p)),p)
print(ps,"\n")
print(ps["2026Q3"],"\n")
print(ps["2026"],"\n")
print(ps["2025":"2026"])
#Comment Someone can change period index to datetime index 
idx = p.to_timestamp()
print(idx,"\n")
# Also someone can change the datetime to period index 
idx2 = idx.to_period()
print(idx2,"\n")

#Exercise 
# Create a DataFrame with 5 quarters in a row with revenue, expenses, and profit
quarters = pd.period_range(start="2025Q1", periods=5, freq="Q")
data = {
    "Revenue": [15000, 16000, 17000, 18000, 19000],
    "Expenses": [5000, 6000, 7000, 8000, 9000],
    "Profit": [10000, 10000, 10000, 10000, 10000]
}
df = pd.DataFrame(data, index=quarters)
print("DataFrame with 5 quarters:\n", df)
# df = df.T
# print("\n",df)
df["Start_Date"] = df.index.map(lambda x: x.start_time)
df = df[["Start_Date", "Revenue", "Expenses", "Profit"]]
print("\n", df)
# Create a crosstab of Revenue and Expenses
df1 = pd.crosstab(df["Revenue"], df["Expenses"], margins=True)
print("\n","Crosstab of Revenue and Expenses:\n", df1)
df["End_Date"] = df.index.map(lambda x: x.end_time)
df["Start_Date"] = df["Start_Date"].dt.date
df["End_Date"] = df["End_Date"].dt.date
df = df[["Start_Date", "End_Date", "Revenue", "Expenses", "Profit"]]
print("\n", df)
