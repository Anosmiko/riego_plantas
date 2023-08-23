import streamlit as st

st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")

st.title("Projects")



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

# Specify the year and month
year = 2023
month = 8

# Create a TextCalendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)  # You can change the first weekday if desired

# Generate a matrix of zeros for the entire month
days_in_month = cal.monthdays2calendar(year, month)
matrix = np.zeros((len(days_in_month), 7))

# Find the week and day of the 22nd
for week_num, week in enumerate(days_in_month):
    for day_num, (day, weekday) in enumerate(week):
        if day == 22:
            matrix[week_num, weekday] = 1

# Create a DataFrame and plot it using seaborn
df = pd.DataFrame(matrix, columns=calendar.day_abbr)
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="coolwarm", cbar=False)
plt.title(f"Calendar for {calendar.month_name[month]} {year} with Highlighted 22nd")
plt.show()