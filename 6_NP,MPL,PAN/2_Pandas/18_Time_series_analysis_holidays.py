import pandas as pd
import numpy as np
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday
from pandas.tseries.offsets import CustomBusinessDay, DateOffset
from datetime import datetime
from dateutil.relativedelta import MO, TH

# Reading the CSV file
df = pd.read_csv(
    "/home/mehrajofficial000/AI_Engineering/6_NP,MPL,PAN/apple_stock_prices.csv",
    usecols=["Price", "Open", "High", "Low"],
)
rng = pd.date_range(start="2024-01-01", periods=64, freq="B")
df = df.set_index(rng)
df = df.rename_axis("Date")
print("1__\n", df, "\n")

# Defining the US Federal Holiday Calendar
class USFederalHolidayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("New Year's Day", month=1, day=1, observance=nearest_workday),
        Holiday(
            "Birthday of Martin Luther King, Jr.",
            start_date=datetime(1986, 1, 1),
            month=1,
            day=1,
            offset=DateOffset(weekday=MO(3)),
        ),
        Holiday("Washington's Birthday", month=2, day=1, offset=DateOffset(weekday=MO(3))),
        Holiday("Memorial Day", month=5, day=31, offset=DateOffset(weekday=MO(-1))),
        Holiday(
            "Juneteenth National Independence Day",
            month=6,
            day=19,
            start_date="2021-06-18",
            observance=nearest_workday,
        ),
        Holiday("Independence Day", month=7, day=4, observance=nearest_workday),
        Holiday("Labor Day", month=9, day=1, offset=DateOffset(weekday=MO(1))),
        Holiday("Columbus Day", month=10, day=1, offset=DateOffset(weekday=MO(2))),
        Holiday("Veterans Day", month=11, day=11, observance=nearest_workday),
        Holiday("Thanksgiving Day", month=11, day=1, offset=DateOffset(weekday=TH(4))),
        Holiday("Christmas Day", month=12, day=25, observance=nearest_workday),
    ]

# Defining a custom holiday calendar


class My_Birthday(AbstractHolidayCalendar):
    rules = [Holiday("My Birthday",month=12,day=3)]
My_Birthday_class = My_Birthday()
my_birth = CustomBusinessDay(calendar=My_Birthday_class)
rng = pd.date_range(start='2024-11-30',periods=64,freq=my_birth)
df = df.set_index(rng)
df = df.rename_axis("Date")  
print("3__\n",df,"\n") # 03red december is removed 


# What if i want to get holiday on next bussiness day when it overlapse the weekends days 

class My_Birthday(AbstractHolidayCalendar):
    rules = [Holiday("My Birthday",month=12,day=7,observance=nearest_workday)]
My_Birthday_class = My_Birthday()
my_birth = CustomBusinessDay(calendar=My_Birthday_class)
rng = pd.date_range(start='2024-11-30',periods=64,freq=my_birth)
df = df.set_index(rng)
df = df.rename_axis("Date")  
print("3__\n",df,"\n") # 06 is removed 
# someone can also make the the custom bussinessday 
b = CustomBusinessDay(weekmask="Sun Mon")
rng = pd.date_range(start="2024-12-31",periods=64,freq=b)
print("\n",rng)
df = df.set_index(rng)
df = df.rename_axis("Date")
print("4__\n",df,"\n") 