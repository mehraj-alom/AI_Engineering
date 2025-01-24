import pandas as pd 
import numpy as np
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/replace_function_practice_with_units.csv")
print("1__\n",df,"\n")
df.set_index("Date",inplace=True)
print("After Index update\n",df,'\n')
df.loc["2025-01-03", "Temperature (°C)"] = -9999
df.loc["2025-01-03","Windspeed (mph)"] = np.NaN
df.loc["2025-01-03","Event"] = np.NaN
print("after loc used\n",df,"\n")
#replacing -9999 with np.nan
df = df.replace(-9999,np.NaN)
print("4__\n",df,"\n")
#Working with score 
df = df.replace(["Excellent","Good","Average","Poor"],[5,4,3,2])
print("5__\n",df,"\n")
#replace the Nan now 
df = df.replace({
    "Temperature (°C)" : -9999,
    # "Windspeed (mph)" : None,
    "Score" : 2
    },np.NaN)
print("6__\n",df,"\n")
#filling na values 
df = df.fillna({
    "Temperature (°C)" : 0,
    "Windspeed (mph)" : 0,
    "Event" :  "Sunny",
    "Score" : 1
})
print("7__\n",df,"\n")
print("8__\n",np.mean(df["Score"]),"\n")


#REGEX (Reguler Expression)
#Removing char like >c , mph  from temp and wind
# new_df = df.replace('[A-Za-z°]','',regex=True).replace('',np.NaN).astype(float)
df = df.replace({
    "Temperature (°C)": '[A-Za-z°]',
    "Windspeed (mph)":'[A-Za-z°]'
},'',regex=True)
df["Temperature (°C)"] = df["Temperature (°C)"].replace('',np.NaN).astype(float)
df["Windspeed (mph)"] = df["Windspeed (mph)"].replace('', np.NaN).astype(float)
print("9__\n",df,"\n")
# problem occured is event also got All Nan values 
print("Temp_Median \n",np.median(df["Temperature (°C)"]),"\n")
print("Wind_Median \n",np.median(df["Windspeed (mph)"]),"\n")
