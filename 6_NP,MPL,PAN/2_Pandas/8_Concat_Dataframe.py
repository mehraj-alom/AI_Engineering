import pandas as pd
India_data = pd.DataFrame({
    "Day" : ["Sunday","Monday","Tuesday","Wednesday"],
    "Temperature" :[25,56,34,67],
    "Wind_Speed": [13,14,15,16]
})
Nepal_data = pd.DataFrame({
    "Day" : ["Sunday","Monday","Tuesday","Wednesday"],
    "Temperature" :[5,5,3+4,7],
    "Wind_Speed": [3,34,9,6]
})
Pakistan_data = pd.DataFrame({
    "Day" : ["Sunday","Monday","Tuesday","Wednesday"],
    "Temperature" :[30,40,35,45],
    "Wind_Speed": [10,20,15,25]
})

Bangladesh_data = pd.DataFrame({
    "Day" : ["Sunday","Monday","Tuesday","Wednesday"],
    "Temperature" :[28,38,33,43],
    "Wind_Speed": [12,22,18,28]
})
print("1__Nepal_data\n",Nepal_data,"\n")
print("2__India's_data\n",India_data,"\n")
print("3__Pakistan's_data\n",Pakistan_data,"\n")
print("4__Bangladesh's_data\n",Bangladesh_data,"\n")

#concating these dataframes
whole = pd.concat([India_data, Bangladesh_data, Pakistan_data, Nepal_data], ignore_index=True)
print(whole)

# grouping the data
x = whole.groupby("Day")
for day, days_df in x:
    print(day, "__\n")
    print(days_df, "\n")

print("Temperature(Mean) on wednesday \t :",x.get_group("Wednesday")["Temperature"].mean())
# Concate and keep the keys alongside
whole = pd.concat([India_data, Bangladesh_data, Pakistan_data, Nepal_data], ignore_index=False,keys=["India","Bangladesh","Pakistan","Nepal"])
print("4___\n",whole,"\n")

#Group on axis 1 (append by columns)
whole = pd.concat([India_data, Bangladesh_data, Pakistan_data, Nepal_data], ignore_index=False,axis=1)
print("5__\n",whole,"\n")
# concat with series 
series = pd.Series(["Rainy","Wind","foggy","sunny"],name="Weather")
Sunday_df = x.get_group("Sunday").reset_index(drop=True)
con = pd.concat([Sunday_df,series],axis=1)
print("6__\n",con,"\n")