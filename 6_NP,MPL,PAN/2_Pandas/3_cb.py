import pandas as pd 
df = pd.read_csv("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/weather_data.csv")
print("1..\n",df,"\n")

# Different ways to create Dataframe 
D_d = pd.read_excel("/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/disease_detection_data.xlsx")
print("2__\n",D_d,"\n")


#*********************************************************************practice 
print("3__\n",D_d[D_d["Duration (Days)"] == D_d["Duration (Days)"].max()],"\n")
print("4__\n",D_d[["Patient ID","Symptoms"]][D_d["Duration (Days)"]==D_d["Duration (Days)"].max()-1],"\n")
print("5__\n",D_d.head(7),"\n\n",D_d.tail(3),"\n")
D_d.set_index("Patient ID",inplace=True)
print("7__\n",D_d,"\n")
print("8__\n",D_d.loc["P009"],"\n") # LOC only works with the key , it is used to look the whole row using key
D_d.reset_index(inplace=True)
print("9__\n",D_d["Age"].median(),"\n")
print("10__\n",D_d["Age"].mean(),"\n")
print("11__\n",D_d["Duration (Days)"].mean(),"\n")

## BACK TO THE TOPIC (DATAFRAME CREATION )
# using native dictionary
My_data = {
    "Roll No" :[1,2,3,4,5,6],
    "Class" :["I","II","III","IV","V","VI"],
    "Avg marks": [90,78,56,89,67,100]
}
My_d = pd.DataFrame(My_data)
print("12__\n",My_d,"\n")
My_d.set_index("Class",inplace=True)
print("13__\n",My_d,"\n")

# Using Tuples List 
More = [
    (1, "Arjun", 27, 25000),
    (2, "Bhavesh", 30, 30000),
    (3, "Chirag", 22, 22000),
    (4, "Divya", 25, 27000),
    (5, "Esha", 28, 28000)
]
more1 = pd.DataFrame(More,columns=["Serial","Name","Age","Salary"])# Names of columns must be given
print("14__\n",more1,"\n")
more1.set_index("Serial",inplace=True)
# using dictionari's list 
my_list = [
    {"Name" : "Hello","Work":"Admin","exp":"2 Years"},
    {"Name" : "John","Work":"Developer","exp":"3 Years"},
    {"Name" : "Jane","Work":"Designer","exp":"4 Years"},
    {"Name" : "Mike","Work":"Manager","exp":"5 Years"},
    {"Name" : "Anna","Work":"Tester","exp":"1 Year"},
    {"Name" : "Tom","Work":"Support","exp":"2 Years"},
    {"Name" : "Sara","Work":"HR","exp":"3 Years"}
]
my_list_1 = pd.DataFrame(my_list)
my_list_1.set_index("Work",inplace=True)
print("15__\n",my_list_1,"\n")
