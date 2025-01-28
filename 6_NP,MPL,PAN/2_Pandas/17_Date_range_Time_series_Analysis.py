import pandas as pd 
import numpy as np 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/apple_stock_prices.csv",usecols=["Price","Open","High","Low"])
print("1__\n",df.head(10),"\n")
# rng = np.random.randint(1,100,20)
# print(rng)
rng = pd.date_range(start="2024-01-01",periods=64,freq="B")
df = df.set_index(rng)
print("2__\n",df,"\n")
print(rng,"\n")
# import matplotlib.pyplot as plt
# df['Low'].plot(title='Apple Stock Low Prices')
# plt.xlabel('Date')
# plt.ylabel('Low Price')
# plt.show()
#when there are wholes in data we fill it using asfreq 

print("4__",df.asfreq('D',method='pad'),"\n")