import numpy as np

import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
x = np.linspace(0, 2 * np.pi, len(days))
temperatures = 22 + 3 * np.sin(x)
humidity = 30 + 15 * np.sin(x + np.pi / 4)
precipitation = 0.3 + 0.3 * np.sin(x + np.pi / 2)
plt.title("Weather Data",fontsize=12,color="Green")
plt.plot(days, temperatures, "g-o", label="Temperature (°C)")
plt.plot(days, humidity, "r-o", label="Humidity (%)")
plt.plot(days, precipitation, "b-o", label="Precipitation (mm)")
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend(loc="upper right",fontsize=10) # Normally it stays at the best location 
plt.grid(True, linestyle="dashdot", alpha=0.4)
plt.show()