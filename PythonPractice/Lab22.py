import pandas as pd

# represent this data using a Pandas Series.
# Input:
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

print("_____________Answer 1_____________")
data = pd.Series(exam_scores, index = students, name = 'Exam Scores')
print(data)


# represent this expense data using a Pandas Series.
# Input:
# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]

print("\n_____________Answer 2_____________")
data2 = pd.Series(expenses, index = categories, name = 'Monthly Expenses (USD)')
print(data2)


# represent this data using Pandas Series.
# Input:
# Months in a year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
# Monthly energy consumption data (example data in kilowatt-hours for electricity and therms for gas)
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]

print("\n_____________Answer 3_____________")
data3 = pd.Series(electricity_usage, index = months, name = 'Electricity Usage (kWh)')
print("Electricity Usage:\n", data3, "\n")

data4 = pd.Series(gas_usage, index = months, name = 'Gas Usage (kWh)')
print("Gas Usage:\n", data4)


# represent this data using a Pandas Series.
# Input:
# Months in a year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
# Monthly advertising revenue data (example data in USD)
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]

print("\n_____________Answer 4_____________")
data5 = pd.Series(revenue, index = months, name = 'Monthly Advertising Revenue (USD)')
print(data5)

print("\n__________ChatGPT code____________")
# first question
# Using ChatGPT generate the python code to solve the same problem
# Hi! I have two columns with some dummy value. I want to create a line plot of the
# opening, closing stock prices of SBI between two specific dates using a pandas
# plot.Can you generate a complete code for me?
# After generating the code using chatgpt, run the code, display the output and give your
# conclusion.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate dummy data
dates = pd.date_range(start="2024-01-01", end="2024-01-10")
data = {
    "Opening_Price": np.random.uniform(500, 550, len(dates)),
    "Closing_Price": np.random.uniform(500, 550, len(dates)),
}
df = pd.DataFrame(data, index=dates)

# Step 2: Select the date range you want to plot
start_date = "2024-01-03"
end_date = "2024-01-07"

# Filter the data within the date range
filtered_df = df.loc[start_date:end_date]

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(filtered_df.index, filtered_df["Opening_Price"], marker='o', label='Opening Price')
plt.plot(filtered_df.index, filtered_df["Closing_Price"], marker='o', label='Closing Price')

# Step 4: Customize the plot
plt.title('SBI Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

# second question
# Using ChatGPT generate the python code to solve the same problem
# Scenario: Analyzing Stock Prices
# Suppose you are an investor interested in analyzing the stock prices of a particular
# company over a year. You have collected daily closing prices for that company's stock,
# and you want to perform some analysis like Calculate the average daily return,Find the
# date with the highest closing price and also generate a line chart using Pandas Series.
# Further, you need to get some inference out of the chart.
# Create a ChatGPT prompt to generate the code for this scenario. Based on the code
# generated, ask ChatGPT to give the conclusion/inference.
# Note. You can provide the data to ChatGPT in the form of a list or dictionary or ask it to
# use sample data
print("\n_________ChatGPT Answer 2_________")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Provided stock data (dictionary format)
stock_data = {
    '2023-01-01': 150.0, '2023-01-02': 152.5, '2023-01-03': 148.0, '2023-01-04': 155.0, '2023-01-05': 157.5,
    '2023-01-06': 160.0, '2023-01-07': 158.0, '2023-01-08': 162.0, '2023-01-09': 161.5, '2023-01-10': 163.0,
    # Additional data would be included here for the entire year
}

# Convert the dictionary to a Pandas Series
dates = pd.to_datetime(list(stock_data.keys()))
prices = pd.Series(list(stock_data.values()), index=dates)

# 1. Calculate the average daily return
daily_returns = prices.pct_change().dropna()
average_daily_return = daily_returns.mean()

# 2. Find the date with the highest closing price
max_price_date = prices.idxmax()
max_price_value = prices.max()

# 3. Generate a line chart to visualize the stock prices over time
plt.figure(figsize=(12, 6))
plt.plot(prices.index, prices, marker='o', linestyle='-', color='b')
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.grid(True)
plt.show()

# Output the results
print(f"Average Daily Return: {average_daily_return:.4f}")
print(f"Date with Highest Closing Price: {max_price_date.strftime('%Y-%m-%d')} with price {max_price_value:.2f} INR")
