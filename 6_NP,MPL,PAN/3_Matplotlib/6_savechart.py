import matplotlib.pyplot as plt

# Create lists with home expenses data
categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Entertainment', 'Healthcare', 'Miscellaneous']
amounts = [1200, 150, 300, 100, 50, 200, 100]

# Pie chart 
plt.pie(amounts, labels=categories,radius=1.5,autopct="%0.2f%%",shadow=True,explode=[0,0.2,0,0.3,0,0,0.1],
        startangle=180)
#Explode makes it come out from the bonding 
plt.title = "Home Expanses"
plt.legend()
plt.savefig("piechart.png",bbox_inches="tight",pad_inches=2,transparent=True)