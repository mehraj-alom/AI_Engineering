import pandas as pd 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/weather_data_with_missing_values.csv")
print("1__\n",df,"\n")
df.set_index("Date",inplace=True)
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
a = df.reset_index()
a["Date"] = pd.to_datetime(a["Date"])
a = a.interpolate()
print("8__\n",a.set_index("Date"),"\n")

