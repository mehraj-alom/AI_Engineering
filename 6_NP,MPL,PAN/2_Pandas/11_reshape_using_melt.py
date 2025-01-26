import pandas as pd

# Melt is used to transform or reshape data 
df = pd.DataFrame({
    "Day":["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"],
    "Chicago" :[32,30,28,22,30,20,25],
    "Chennai":[75,77,75,82,83,81,87],
    "Berlin":[41,43,45,38,30,45,47]
})
print("1__\n",df,"\n")
melted = pd.melt(df,id_vars=["Day"])
print("2__\n",melted,"\n") # In Id_vars we do keep the column that we want to keep intect (Not change accordigly )
print("3__\n",melted[melted["variable"]=="Chicago"])
print("3__\n",melted[melted["variable"]=="Chicago"])
# Someone can change the name of the variable as well 
melted =pd.melt(df,id_vars=["Day","Berlin"],var_name="City",value_name="Temperature")
print("2__\n",melted,"\n")
