import numpy as np
# Ques.1 Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with
# extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below
# 15 degrees Celsius (cold day).
# Input:
print("__________Answer 1__________\n")
temperatures = np.array([35.5, 4.2, 36.8, 29.3, -1.0, 38.7, 3.1, 18.5, 22.8, 37.2, -5.8])
print("Cold Days: ")
print("Day\t"+"\tTemperature(in Celsius)")
for i in range(len(temperatures)):
    if temperatures[i]<5:
        print(i , "\t\t", temperatures[i])

print("\nHot Days: ")
print("Day\t"+"\tTemperature(in Celsius)")
for i in range(len(temperatures)):
    if temperatures[i]>35:
        print(i , "\t\t", temperatures[i])


# 2. Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and
# reporting purposes.
# Input:
print("\n__________Answer 2__________")
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
quarter = len(monthly_sales)/4
count = 1
for i in range(len(monthly_sales)):
    if i % quarter == 0:
        print(f"\nQuarter {count} Sales (in thousand of dollars): ")
        count+=1
    print(monthly_sales[i], end= " ")


# 3. Suppose you have a dataset containing customer data, and you want to split this data into two groups: one group for customers who made a purchase in the
# last 30 days and another group for customers who haven't made a purchase in the last 30 days.
# Input:
print("\n\n__________Answer 3__________")
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
arr1 = []
arr2 = []
for (i,j) in zip(range(len(customer_ids)),range(len(last_purchase_days_ago))):
    if last_purchase_days_ago[j] > 30:
        arr1.append(customer_ids[i])
    else:
        arr2.append(customer_ids[i])

print("\nActive customers (Last Purchase <= 30 days ago): ")
for i in arr2:
    print(i, end=" ")
print("\nInactive customers (Last Purchase > 30 days ago): ")
for i in arr1:
    print(i, end=" ")


# 4.Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time
# employees. You want to combine this data to create a comprehensive employee dataset for HR analysis.
# Input:
print("\n\n__________Answer 4__________\n")
# Employee data for full-time employees
full_time_employees = np.array([[101, 'John Doe', 'Full-Time', 55000],[102, 'Jane Smith', 'Full-Time', 60000],[103, 'Mike Johnson', 'Full-Time', 52000]])
# Employee data for part-time employees
part_time_employees = np.array([[201, 'Alice Brown', 'Part-Time', 25000],[202, 'Bob Wilson', 'Part-Time', 28000],[203, 'Emily Davis', 'Part-Time', 22000]])

concat = np.concatenate((full_time_employees,part_time_employees))
print("Combined Employee Data")
for i in concat:
    print("Employee ID:", i[0], "Name:", i[1], "Type:", i[2], "Salary:", i[3])










