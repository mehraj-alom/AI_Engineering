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