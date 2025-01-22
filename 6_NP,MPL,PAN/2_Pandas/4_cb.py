# More about read and write excel csv file 
import pandas as pd 
a = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv")
print("1__\n",a,"\n")
a.set_index("Year",inplace=True)
print("2__\n",a,"\n")
a.reset_index()
# If the file not containng aany header we can add by keeping header is None followed by names of headers 
b = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv",header=None, names= ["Year","Revenue","Cost","Profit"])
print(b)
# To read some line from the dataframe  using nrows =  ;
c = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv",nrows=4)
print("4__\n",c,"\n")
# I want to make "Nan" as NaN(not a number ) 
d = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv",na_values=["NaN"])
print("5__\n",d,"\n\n")
d = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv",na_values={
    "Revenue":["Item A","Item B"],
    "Cost" :["Miscellaneous","Supplies"]
})
print("\n ",d,"\n")
# Profit and revenue cannot be negative but the csv file contains this so we need to take care of it 
e = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv")
e["Revenue"] = pd.to_numeric(e["Revenue"],errors="coerce").fillna(0)
e["revenue"] = e["Revenue"].apply(lambda x : 0 if x < 0 else x )
print("6__\n",e,"\n")
#              another one 
f = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_data_with_strings.csv")
f["Profit"] = pd.to_numeric(f["Profit"],errors="coerce").fillna(0)
f["Profit"] = f["Profit"].apply(lambda x : 0 if x < 0 else x )
f["Revenue"] = pd.to_numeric(f["Revenue"],errors="coerce").fillna(0)
f["Revenue"] = f["Revenue"].apply(lambda x: 0 if x < 0 else x)
print("7__\n",f,"\n")
if "Year" in f.columns:
    print(f.describe().drop(columns=["Year"]))
else:
    print(f.describe()) 



# *********************** Writing to Csv file 
# f.to_csv("Written.csv",index = False)
# f.to_csv("only_two_col_and_Noheader.csv",header=None,columns=["Year","Revenue"]) Commented beacuse  memory taking 

# ********************** WWriting to excel file 
Stocks_data = pd.DataFrame({
    "Date": ["2025-07-01", "2025-07-03", "2025-07-05"],
    "Price": ["Nan", 150, -300],
    "Profit": [10, 15, 20],
    "Bought_time": ["10:00", "11:00", "12:00"]
})
weather_data = pd.DataFrame({
    "Date": ["2025-07-01", "2025-07-02", "2025-07-03"],
    "Temperature": [30, 4000, 31],
    "Humidity": [70, 65, 75],
    "Wind Speed": [5, 7, -2]
})
weather_data.set_index("Date",inplace=True)
Stocks_data.set_index("Date",inplace=True)
print("9__\n",weather_data,"\n")
print("10__\n",Stocks_data,"\n")
# converting (munging/wrangling)
weather_data["Temperature"] = weather_data["Temperature"].apply(lambda x : 0 if x > 100 else x)
weather_data["Wind Speed"] = weather_data["Wind Speed"].apply(lambda x: 0 if x < 0 else x)
print("11__\n",weather_data,"\n")
Stocks_data["Price"] = Stocks_data["Price"].apply(lambda x : "Wrong" if x == "Nan" or x < 0 else x)
print("12__\n",Stocks_data,"\n")
#writing excel file
# with pd.ExcelWriter("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/financial_and_weather_data.xlsx") as writer:
#     Stocks_data.to_excel(writer, sheet_name="Stocks Data")
#     weather_data.to_excel(writer, sheet_name="Weather Data") # Commented beacuse memory taking 