# Import necessary libraries
import numpy as np  # NumPy for numerical operations and array handling
import matplotlib.pyplot as plt  # Matplotlib for creating visualizations

# Data
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])  # X-axis values (independent variable)
y = np.array([35, 25, 55, 45, 75, 65, 95, 85, 115, 105, 135, 125])  # Y-axis values (dependent variable)

# Create the plot
plt.figure(figsize=(8, 5))  # Create a new figure with a specific size (width=8, height=5 inches)

# Plot the data
plt.plot(
    x, y,  # X and Y data to plot
    color="green",  # Color of the line and markers
    marker="o",  # Marker style (circles in this case)
    linestyle="-",  # Line style (solid line)
    markersize=8,  # Size of the markers
    label="Data Points",  # Label for the legend
    alpha=0.1  # Transparency of the line and markers (0 = fully transparent, 1 = fully opaque)
)

# Add labels and title
plt.title("Improved Plot for Beginners", fontsize=16)  # Title of the plot with font size 16
plt.xlabel("X Values", fontsize=14)  # Label for the X-axis with font size 14
plt.ylabel("Y Values", fontsize=14)  # Label for the Y-axis with font size 14

# Add grid for better readability
plt.grid(True, linestyle="--", alpha=0.7)  # Enable grid with dashed lines and transparency of 0.7

# Add a legend
plt.legend()  # Display the legend to describe the data points

# Show the plot
plt.show()  # Render the plot on the screen