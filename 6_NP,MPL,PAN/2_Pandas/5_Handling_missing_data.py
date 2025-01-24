import pandas as pd 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/weather_data_with_missing_values.csv")
print("1__\n",df,"\n")
# df.set_index("Date",inplace=True)
print("2__\n",df,"\n")
# handling missing values with fillna 
print(df.describe())
new_df = df
new_df = new_df.fillna(
    {
        "Temperature (°C)": 0,
        "Humidity (%)" : 0,
        "Wind Speed (km/h)": "Missing"
    }
)
print("3__\n",new_df,"\n")
new_df = new_df.ffill() 
print("4__\n",new_df,"\n")
new_df["Wind Speed (km/h)"] = new_df["Wind Speed (km/h)"].apply(lambda x : 0 if x == "Missing" else x)
print("5__\n",new_df,"\n")
# Interesting 
new_df.replace(0, None, inplace=True)
new_df = new_df.fillna(method="ffill")
print("6__\n",new_df,"\n")
# using bfill 
# a = df.reset_index()
# a["Date"] = pd.to_datetime(a["Date"])  # Error 
# a = a.interpolate()
# print("8__\n",a.set_index("Date"),"\n")


d = df.interpolate()
print("7__\n",d,"\n")
print(type(df["Date"]))
df["Date"]=pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
d = df.interpolate(method="time")
print("8__\n",d,"\n")
df.reset_index(inplace=True)
print(type(df["Date"]))


# Drop rows 
new_df = df.dropna()
print("\n\n ",new_df)
new_df = df.dropna(how="all")
print("\n\n ",new_df)
new_df = df.dropna(thresh=1) # it means it will keep the row if one value is NAn
print("\n\n ",new_df)
new_df = df.dropna(thresh=6)
print("\n\n ",new_df)

#add dates in between or end or starting 
dt = pd.date_range("2025-01-01","2025-01-18")
idx = pd.DatetimeIndex(dt)
a = df.reindex(idx)
print("\n\n",a)     # Confusion remaining 




