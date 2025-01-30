"""
Shifts the values in the specified column of a pandas DataFrame and logs the changes.

Parameters:
-----------
df : pandas.DataFrame
    The DataFrame containing the data to be shifted.
column_name : str
    The name of the column to shift.
shift_by : int
    The number of periods to shift. Positive values shift down, negative values shift up.
log : bool, optional
    If True, logs the changes made to the DataFrame. Default is False.

Returns:
--------
pandas.DataFrame
    A new DataFrame with the specified column shifted.

Notes:
------
- This function creates a new DataFrame with the specified column shifted by the given number of periods.
- If `log` is set to True, the function will print the original and shifted values of the specified column for comparison.
- The original DataFrame remains unchanged.
"""

import pandas as pd
import numpy as np

# Set the seed for reproducibility to ensure the same random values each time the script runs
np.random.seed(0)

# Create a sample DataFrame with random prices and business days as the index
df = pd.DataFrame({
    "Date": pd.date_range(start="2026-01-01", periods=10, freq="B"),  # 'B' stands for business days (Monday-Friday)
    "Price": np.random.randint(100, 200, 10)  # Generate 10 random integer prices between 100 and 200
})

# Set "Date" as the index, making it easier to perform time-based operations
df.set_index("Date", inplace=True)

# Display the original DataFrame
print("Original DataFrame:\n", df, "\n")

# Function to shift values in a specified column and optionally log the changes
def shift_and_log(df, column_name, shift_by, log=False):
    """
    Shifts the specified column in a DataFrame and logs the changes if requested.

    Args:
    df (pandas.DataFrame): The input DataFrame.
    column_name (str): The column to shift.
    shift_by (int): The number of positions to shift the column.
    log (bool, optional): If True, prints the original and shifted DataFrame. Default is False.

    Returns:
    pandas.DataFrame: A new DataFrame with the shifted column.
    """
    # Copy the original DataFrame to avoid modifying it directly
    original = df.copy()
    shifted = df.copy()

    # Shift the specified column by the given number of periods
    shifted[column_name] = shifted[column_name].shift(shift_by)

    # Log changes if requested
    if log:
        print("Original DataFrame:\n", original, "\n")  # Print original DataFrame
        print("Shifted DataFrame:\n", shifted, "\n")  # Print shifted DataFrame
    
    return shifted

# Shift the "Price" column by 1 period downward and log the changes
shifted_df = shift_and_log(df, "Price", 1, log=True)

# ============================ Arithmetic Operations ============================

# Create a new column "Changed Price" containing the shifted price values
df["Changed price"] = shifted_df["Price"]

# Calculate the absolute price difference between the original and shifted prices
df["Price Difference"] = df["Price"] - df["Changed price"]

# Calculate the percentage difference relative to the original price
df["Price Difference (%)"] = (df["Price Difference"] * 100) / df["Price"]

# Print the updated DataFrame with the calculated differences
print("\nUpdated DataFrame with Price Difference calculations:\n", df)

# ============================ Shifting Dates ============================

# Create a copy of the DataFrame to shift the index (dates)
df_shifted_dates = df.copy()

# Shift the index forward by 1 business day to simulate a date shift
df_shifted_dates.index = df_shifted_dates.index.shift(1, freq='B')

# Print the DataFrame with shifted dates
print("\nDataFrame with Shifted Dates:\n", df_shifted_dates)
