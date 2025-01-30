"""
This function takes a datetime object and returns a formatted string representation of the date and time.

Args:
    dt (datetime): A datetime object representing the date and time to be formatted.

Returns:
    str: A string representing the formatted date and time.

# There are two types of datetime objects in Python:
# 1. Naive datetime: These objects do not contain any timezone information. They are not aware of any time zone and are typically used for representing local time.
# 2. Aware datetime: These objects contain timezone information. They are aware of the time zone and can be used to represent time in different time zones accurately.
"""

import pandas as pd
from pytz import all_timezones

# Create a DataFrame with 8 entries, representing daily price and profit data
df = pd.DataFrame({
    "Date": pd.date_range(start='2023-01-01', periods=8, freq='D'),
    "Price": [100, 150, 200, 250, 300, 350, 400, 450],
    "Profit": [10, 15, 20, 25, 30, 35, 40, 45]
})

# Set "Date" column as the index
df = df.set_index("Date")

# Display the initial DataFrame with naive datetime (no timezone awareness)
print("1__\n", df, "\n")
print("2__\n", df.index, "\n")  # This is a naive datetime index (no timezone info)

# Convert the naive datetime index to a timezone-aware datetime (Asia/Kolkata)
df = df.tz_localize(tz="Asia/Kolkata")
print("2__\n", df.index, "\n")  # Now the index has timezone information

# Convert the timezone-aware datetime from "Asia/Kolkata" to "US/Eastern"
df = df.tz_convert('US/Eastern')
print("3__\n", df.index, "\n")  # Timezone has now been converted to US/Eastern

# Print all available timezones (commented out to avoid excessive output)
# print("3__\n", all_timezones, "\n")

# Display all available timezones
for time in all_timezones:
    print(time)

# Convert the timezone back to "Asia/Kolkata"
df = df.tz_convert(tz="Asia/Kolkata")
print("4__\n", df, "\n")  # The index is now back in "Asia/Kolkata" timezone

# Generate a new date range with hourly intervals, including timezone information
rng = pd.date_range(start="2026-12-1", periods=10, freq="H", tz="Asia/Kolkata")
print("6__\n", rng, "\n")  # Displays a date range with timezone-aware timestamps

