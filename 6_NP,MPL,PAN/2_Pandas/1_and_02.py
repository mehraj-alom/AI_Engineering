import pandas as pd 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/weather_data.csv")
print("1")
print(df)
# Shape of the dataframe 
print("2")
print(df.shape)
rows, columns = df.shape # this can also be done like this 
print("3","\n")
print(rows)
print("4")
print(columns)
# To get some rows instaed of all 
print(df.head(3)) # it gives first three rows 

print(df.tail(3)) # this gives last three rows

# iNDEXING AND SLICING 
print("\n")
print(df[2:5])
print("\n")
print(df["Temperature (°C)"])
print("\n")
print(df[["Wind Speed (km/h)","Event"]])
print(df.Event)
# Max 
print(df[["Temperature (°C)","Wind Speed (km/h)"]].max(),"\n")
# Min
print(df[["Temperature (°C)","Wind Speed (km/h)"]].min(),"\n")
# Mean or avg 
print(df[["Temperature (°C)","Wind Speed (km/h)"]].mean(),"\n")
# median 
print(df["Temperature (°C)"].median(),"Median \n")
# standerd deviation 
print(df[["Temperature (°C)","Wind Speed (km/h)"]].std())

# Describe method --> It gives all the description such as min, max , mode , median , std etc.. for all 
# the numeric value rows in the table or dtatframe  
print(df.describe())

# Conditional execution 
print(df["Temperature (°C)"] > 12) # returns the vales with either true or false
print(df[df["Temperature (°C)"]>12],"\n") # conditinally giving the output 
# Q. give me the day when the temperature was maximum 
print(df[df["Temperature (°C)"] == df["Temperature (°C)"].max()],"\n")
print(df[["Date", "Temperature (°C)"]][df["Temperature (°C)"] == df["Temperature (°C)"].max()])


# Set index method --> it sets the passed value as the index 

df.set_index("Date",inplace=True)
print(df,"\n")
print(df.loc["2025-01-08"])  # What is loc function does ????
# to reset the index 
df.reset_index(inplace=True)
print(df)
