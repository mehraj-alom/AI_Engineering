import pandas as pd 
# Creating two sample dataframes with city names
df1 = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'population': [8419000, 3980000, 2716000, 2328000]
})

df2 = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'San Francisco', 'Seattle'],
    'area': [468.9, 503, 121.4, 83.9]
})

# Merging the dataframes on the 'city' column
merg = pd.merge(df1,df2,on="city",how='inner')
print("1__\n",merg,"\n") # This only merges the common rows (Intersection)
merg = pd.merge(df1,df2,on="city",how='outer')
print("2__\n",merg,"\n") # Union 
merg = pd.merge(df1,df2,on="city",how='left')
print("3__\n",merg,"\n")
merg = pd.merge(df1,df2,on="city",how='right',indicator=True) # This indicates where the data came from
print("4__\n",merg,"\n")

# When the column name from differnt dataframe are same it just add _x and _y 
df3 = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'temperature': [60, 75, 55, 80],
    'humidity': [65, 70, 75, 80]
})

df4 = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'San Francisco', 'Seattle'],
    'humidity': [65, 70, 75, 80],
    'temperature': [60, 75, 55, 80]
})
merg = pd.merge(df3,df4,on="city")
print("5__\n",merg,"\n") #5__
#            city  temperature_x  humidity_x  humidity_y  temperature_y
# 0     New York             60          65          65             60
# 1  Los Angeles             75          70          70             75 
merg = pd.merge(df3,df4,on="city",suffixes=("_left","_rinht")) # it removes x and y and adds _left _right
print("6__\n",merg,"\n") 
# 6__
#            city  temperature_left  humidity_left  humidity_rinht  temperature_rinht
# 0     New York                60             65              65                 60
# 1  Los Angeles                75             70              70                 75 