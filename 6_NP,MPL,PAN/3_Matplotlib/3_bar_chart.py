import numpy as np
import matplotlib.pyplot as plt

companies = ['Company A', 'Company B', 'Company C', 'Company D']
profits = [25000, 30000, 15000, 35000]
revenues = [100000, 120000, 80000, 140000]
calc = [100000, 30000, 3000, 80000]

bar_width = 0.15
index = np.arange(len(companies))

plt.bar(index, profits, bar_width, color='orange', label='Profits')
plt.bar(index + bar_width, revenues, bar_width, color='blue', label='Revenues')
plt.bar(index + bar_width * 2, calc, bar_width, color="red", label="Calc")

plt.xlabel('Companies')
plt.ylabel('Amount')
plt.title('Profits and Revenues of Companies')
plt.xticks(index + bar_width, companies)
plt.legend()

plt.show()

#For horizontalbar 
plt.barh(index, profits, bar_width, color='orange', label='Profits')
plt.barh(index + bar_width, revenues, bar_width, color='blue', label='Revenues')
plt.barh(index + bar_width * 2, calc, bar_width, color="red", label="Calc")

plt.xlabel('Companies')
plt.ylabel('Amount')
plt.title('Profits and Revenues of Companies')
plt.yticks(index + bar_width, companies)
plt.legend()
plt.show()
