import matplotlib. pyplot as plt
# Lab1: Visualize the daily temperature changes over time in a city.
# Input:
days1 = list(range(1, 32))
# Daily temperature data (replace with your own data)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

plt.plot(temperature, "o-")
plt.xlabel("Day of the Month")
plt.ylabel("Temperature (in Fahrenheit)")
plt.title("Daily temperature changes in July")
plt.show()


# Lab2: Create a line plot to visualize the daily closing prices of a stock over a year.
# Input:
days2 = list(range(1, 78))
# Daily closing prices of a stock (replace with your own data)
stock_prices = [100, 105, 110, 115, 112, 120, 118, 125, 128, 130, 132, 135, 138, 140, 142, 144, 145, 148, 150, 155, 160, 158, 162, 165, 170, 172,
175, 178, 180, 182, 185, 188, 190, 192, 195, 198, 200, 198, 195, 193, 190, 188,185, 182, 180, 178, 175, 172, 170, 168, 165, 162, 160, 158, 155, 152,
150, 148, 145, 143, 140, 138, 135, 132, 130, 128,125, 123, 120, 118, 115, 112, 110, 108, 105, 103, 100]

plt.plot(days2, stock_prices, 'bo-', ms=3)
plt.title("Stock Prices over a year")
plt.xlabel("Day of the year")
plt.ylabel("Stock Price (USD)")
plt.show()


# Lab3: Create a bar chart to represent monthly expenses in different spending categories.
# Input:
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
# Monthly expenses in dollars (replace with your own data)
expenses = [1200, 400, 200, 150, 250]

plt.bar(categories, expenses)
plt.xlabel("Expense category")
plt.ylabel("Monthly Expenses (USD)")
plt.title("Monthly Expense Breakdown")
plt.show()


# Lab4: Create a histogram to represent the distribution of product prices in a retail store.
# Input:
product_prices = [24.99, 34.99, 49.99, 64.99, 39.99, 54.99, 79.99, 99.99, 29.99, 44.99, 59.99, 69.99, 84.99, 109.99, 119.99, 89.99, 74.99, 124.99, 69.99, 54.99]

plt.hist(product_prices, bins=10, edgecolor="black")
plt.xlabel("Product Expenses (USD)")
plt.ylabel("Number of Products")
plt.title("Distribution of Product Prices in a Retail Store")
plt.show()

print("__________ChatGPT Exercise____________")
# Using ChatGPT generate the python code to solve the same problem
# Scenario:
# Suppose you have two columns named regions and sales with some dummy data frame, and you need to generate a bar chart based on these two columns and also
# generate the percentage. Further, you need to get some inference out of the chart. Create a ChatGPT prompt to generate the code for this scenario.
# Based on the code generated, ask ChatGPT to give the conclusion/inference.
# Note. You can provide the data to ChatGPT or ask it to use sample data.

print("ChatGPT prompt will be: \nI have a DataFrame with two columns, 'regions' and 'sales,' containing some dummy data. I want to create a bar chart showing "
      "the sales for each region. Additionally, I'd like to calculate the percentage of total sales for each region and display this information on the chart."
      "After generating the chart, please provide some conclusions or inferences based on the chart.")

# Code used by ChatGPT to do all the task
import pandas as pd
import matplotlib.pyplot as plt

# Creating a dummy DataFrame with 'regions' and 'sales'
data = {'regions': ['North', 'South', 'East', 'West'],
        'sales': [250, 150, 300, 200]}
df = pd.DataFrame(data)

# Calculating percentage of total sales for each region
df['percentage'] = (df['sales'] / df['sales'].sum()) * 100

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['regions'], df['sales'], color='skyblue')

# Adding percentage labels on top of the bars
for bar, percentage in zip(bars, df['percentage']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f'{percentage:.2f}%', ha='center', va='bottom')

plt.title('Sales by Region with Percentage of Total Sales')
plt.xlabel('Regions')
plt.ylabel('Sales')
plt.ylim(0, max(df['sales']) * 1.2)

# Show the plot
plt.show()

# Returning the DataFrame for reference
df


print("\nBased on the code generated, ChatGPT gave the following conclusion/inference: \n"
      "1. East Region Dominance: The East region has the highest sales, contributing 33.33% to the total sales. This suggests that the East region is a strong"
      "market, possibly due to higher demand, better marketing strategies, or more effective sales channels."
      "\n2. Underperformance in South: The South region has the lowest sales, making up only 16.67% of the total sales. This could indicate potential challenges "
      "in this region, such as lower demand, stronger competition, or less effective sales strategies. It might be worthwhile to investigate the causes and "
      "consider targeted improvements."
      "\n3. Moderate Sales in North and West: The North and West regions have moderate sales contributions, with 27.78% and 22.22%, respectively. These regions "
      "are performing adequately but do not stand out. There may be opportunities to boost sales in these areas through enhanced marketing efforts or product "
      "adjustments."
      "\n4. Uneven Sales Distribution: The overall sales distribution across the regions is uneven, with a significant difference between the highest and lowest "
      "performers. This might indicate varying market dynamics or differences in how each region is being approached by the sales team."
      "\n\nIn conclusion, while the East region is performing exceptionally well, there is a need to explore opportunities in the South, North, and West regions "
      "to achieve a more balanced sales distribution.")





