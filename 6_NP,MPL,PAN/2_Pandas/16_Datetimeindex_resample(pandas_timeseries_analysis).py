import pandas as pd 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/apple_stock_prices.csv",parse_dates=["Date"])
print(df)
print("1__\n",type(df["Date"][0]))
print("2__\n",df["Price"].mean())
# print("3__\n",df[])
df = df.set_index("Date")
print(df)
print("3__\n",df.index,"\n")
# Data of only one month (jan) after setting date as datetime index 
print("4__\n",df["2025-01"],"\n")
print("5__\n",df.loc["2025-01"]["High"].mean())
print("5__\n",df["2025-01"].High.mean()) # it is removed so use df.loc instaed of only df
# prices within a range 
print("6__\n",df.loc["2025-01-07":"2025-01-18"],"\n")


# Resampling but why ?
# Because : Resampling in pandas is a powerful method used to change the frequency of your time series data. 
# It allows you to aggregate or summarize data at different time intervals. This is particularly useful for time 
# series analysis, where you might want to analyze data at different granularities (e.g., daily, weekly, monthly).
print("7__", df["High"].resample("M").mean(), "\n")
# import matplotlib.pyplot as plt
# df["High"].resample("M").mean().plot()
# plt.title("Monthly Mean of High Prices")
# plt.xlabel("Date")
# plt.ylabel("Mean High Price")                # execute many times makes the laptop to hang
# plt.show()

import matplotlib.pyplot as plt

# Resample the data to daily frequency and calculate the mean
# daily_mean = df["High"].resample("M").mean()

# # Plot the histogram of the daily mean high prices
# plt.pie(daily_mean.dropna())
# plt.title("Histogram of Daily Mean High Prices")
# plt.xlabel("Mean High Price")
# plt.ylabel("Frequency")
# plt.show()
