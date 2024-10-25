import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Execute the below code and find the output

x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]
plt.plot(x, y)
plt.show()

print("\n_________ChatGPT Exercise__________")

# Step 1: Create sample data
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = np.random.randint(100, 1000, size=len(date_range))  # Random sales between 100 and 1000

# Create a DataFrame
data = pd.DataFrame({'Date': date_range, 'Sales': sales_data})

# Step 2: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Sales'], marker='o')

# Step 3: Customize the plot
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.show()

print("Conclusion Summary:")
print("\n1. Sales Trends: Identify overall trends, noting whether sales are increasing, decreasing, or remaining stable."
"\n2. Seasonal Patterns: Look for consistent spikes or drops in sales during specific months, indicating peak seasons."
"\n3. Anomalies: Detect any unusual sales figures and investigate their causes, such as marketing efforts or market changes."
"\n4. Average Sales: Calculate average sales to set performance benchmarks."
"\nRecommendations"
"\nEnhance Marketing: Focus efforts during peak sales periods."
"\nManage Inventory: Ensure popular products are available during high-demand times."
"\nEngage Customers: Implement promotions during sales dips to boost revenue.")






