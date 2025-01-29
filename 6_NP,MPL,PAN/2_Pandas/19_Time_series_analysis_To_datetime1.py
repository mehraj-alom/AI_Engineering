import pandas as pd
# List of dates in various formats
dates = [
    "2023-10-01",
    "01/10/2023",
    "October 1, 2023",
    "2023.10.01",
    "01-Oct-2023",
    "20231001",
    "2023/10/01",
    "1 Oct 2023",
    "2023-10-01T00:00:00",
    "2023-10-01 00:00:00",
    "abs"
]

# Convert the list of dates to a pandas datetime series
date_series = pd.to_datetime(dates, errors="coerce")

print(date_series)

dates = ["31/12/2002"]
date_series = pd.to_datetime(dates, format="%d/%m/%Y")
print("\n",date_series)
