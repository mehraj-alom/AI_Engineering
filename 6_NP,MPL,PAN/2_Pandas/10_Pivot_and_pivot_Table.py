import pandas as pd 
import numpy as np
# Pivot allows transforming and reshaping data 

data = {
    'city': ['CityA', 'CityB', 'CityC', 'CityA', 'CityB', 'CityC', 'CityA', 'CityB', 'CityC', 'CityA'],
    'temperature': [25, 30, 35, 28, 32, 36, 27, 31, 34, 29],
    'humidity': [45, 50, 55, 48, 52, 56, 47, 51, 54, 49],
    'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05']
}


df = pd.DataFrame(data)
print(df)

new_df = df.pivot(index="date",columns="city",values=["temperature","humidity"])
print("1__\n",new_df,"\n")

# Pivit Table : # And pivot_table allows summirization and aggregation of dataframes 
new_df = df.pivot_table(index="date",columns="city",margins=True) # Margins adds more functionality it make 
# the data to appear as another layer of aggregation  
print("2__\n",new_df,"\n") # By default pivot_table aggregates by mean but we can change it by using aggfunc argument 
new_df = df.pivot_table(index="date",columns="city",aggfunc="sum",margins=True)
print("3__\n",new_df,"\n")
# Grouper function groups the the unique data  (it is assigned to index argument )
print(type(df["date"]))
print(pd.api.types.is_datetime64_any_dtype(df["date"]))
df['date'] = pd.to_datetime(df["date"])
print(pd.api.types.is_datetime64_any_dtype(df["date"]))
print(type(df["date"][0]))
new_df = df[['date', 'temperature', 'humidity']].pivot_table(index=pd.Grouper(freq='D', key='date'))
print("4__\n",new_df,"\n") #Why pd.Grouper Fails with city
# If you attempt to apply pd.Grouper to the city column, Python will throw an error
# because Grouper is not designed to group by non-datetime columns
