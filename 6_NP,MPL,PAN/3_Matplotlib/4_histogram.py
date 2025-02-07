import numpy as np

import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
normal = np.random.normal(loc=90, scale=10, size=100)
prediabetic = np.random.normal(loc=110, scale=10, size=100)
diabetic = np.random.normal(loc=140, scale=10, size=100)

# Combine data
data = [normal, prediabetic, diabetic]
labels = ['Normal', 'Prediabetic', 'Diabetic']

# Plot histogram
plt.hist(data, bins=8, label=labels, alpha=0.7, edgecolor='black',rwidth=0.95,color=["red","pink","white"])
        #  ,orientation="horizontal")
# plt.hist(data, bins=[70,90,110,130,150,200], label=labels, alpha=0.7, edgecolor='black')
# bins can be customized for the range like 20-30 30-40-40-50 etc

# Add titles and labels
plt.title('Blood Sugar Levels of Patients')
plt.xlabel('Blood Sugar Level')
plt.ylabel('Number of Patients')
plt.legend(loc="upper right",fontsize=6)

# Show plot
plt.show()