import pandas as pd
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/cities_weather_data.csv")
print(df,"\n")
x = df.groupby("City")
print("2__\n",x,"\n")
for city,city_df in x :
    print(city)
    print(city_df)
print("\n")
print("3__\n",x.max(),"\n")
print("4__\n",x.mean(numeric_only=True),"\n")
print("5__\n",x.describe(),"\n")

print("\n__",df.shape,"\n")

for city,city_df in x :
    print(city)
    if city == "New York":
        print("Mean Windspeed is ",city_df["Windspeed (mph)"].mean())
    print(city_df)
# getgroup methood 
print("5__\n",x.get_group("Los Angeles"))

print("6__\n",x.max(),"\n")