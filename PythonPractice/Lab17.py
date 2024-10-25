import numpy as np
# 1. How to find the mean of every NumPy array in the given list?
# Input:
print("__________Answer 1__________")
list1 = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]
print("Mean of Array 1:", np.mean(list1[0]),
      "\nMean of Array 2:",np.mean(list1[1]),
      "\nMean of Array 3:",np.mean(list1[2]))


# 2. Compute the median of the flattened NumPy array
# Input:
print("\n__________Answer 2__________")
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original array :", x_odd)
print("Median of Array :", np.median(x_odd))


# 3.Compute the standard deviation of the NumPy array
# Input:
print("\n__________Answer 3__________")
arr = [20, 2, 7, 1, 34]
print("Original array:", arr)
print("Standard Deviation of Array :", np.std(arr))


# 4.Suppose you have a CSV file named 'house_prices.csv' with price information, and you want to perform the following operations:
# ● 1.Read the data from the CSV file into a NumPy array
# ● 2.Calculate the average of house prices.
# ● 3.Identify house price above the average.
# ● 4.Save the list of high prices to a new CSV file.

import csv
import numpy as np

# Generate sample data
np.random.seed(42)
house_ids = np.arange(1, 21)  # 20 house entries
prices = np.random.randint(100000, 500000, size=20)  # Random prices between 100,000 and 500,000

# Save to CSV
with open('house_prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['House_ID', 'Price'])
    for house_id, price in zip(house_ids, prices):
        writer.writerow([house_id, price])

print("CSV file 'house_prices.csv' created successfully.")

import numpy as np
import csv

# Step 1: Read the data from the CSV file into a NumPy array
data = np.genfromtxt('house_prices.csv', delimiter=',', skip_header=1)

# Step 2: Calculate the average of house prices
prices = data[:, 1]  # Extract the price column
average_price = np.mean(prices)

# Step 3: Identify house prices above the average
high_prices = data[prices > average_price]

# Step 4: Save the list of high prices to a new CSV file
with open('high_house_prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['House_ID', 'Price'])
    writer.writerows(high_prices)

print(f"Average house price: {average_price}")
print("CSV file 'high_house_prices.csv' created successfully.")















