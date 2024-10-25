import pandas as pd
import matplotlib.pyplot as plt

# Lab1: Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.
#     Also generate a bar chart based on the result and explain the conclusion.
print("__________Answer1__________")
student_data = pd.DataFrame({'school_code': ['s001','s002','s003','s001','s002','s004'],
                             'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
                             'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill','David Parkes'],
                             'age': [12, 12, 13, 13, 14, 12],
                             'height': [173, 192, 186, 167, 151, 159],
                             'weight': [35, 32, 33, 30, 31, 32],
                             'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']})

print("Original Dataframe:\n", student_data)
print("Class wise number of student count:\n")
data = student_data['class'].value_counts()
print(data)
data.plot(kind='bar', x="Class")
plt.show()


# Lab2: Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school.
# Also generate a horizontal bar chart based on the result and explain the conclusion.
print("\n__________Answer2__________")

print("Original Dataframe:\n", student_data)
print("\nMean, min, and max value of age for each value of the school:")
data2 = student_data['age'].groupby(student_data['school_code']).aggregate(["mean", "min", "max"])
print(data2)

data2.plot(kind='barh', ylabel="school code")
plt.show()

# Lab3: Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean,
# min, and max values of purchase amount (purch_amt) group by customer id (customer_id).Also generate a line chart based on the result and explain the conclusion.
print("\n__________Answer3__________")
orders_data = pd.DataFrame({'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
                            'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                            'ord_date':['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10',
                                        '2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                            'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
                            'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print("Original Dataframe:\n", orders_data)
print("\nMonth wise purchase amount:")
# data4 = orders_data['ord_date'][2].sum
# print(data4)

print(orders_data['ord_date'])
orders_data['ord_date'] = pd.to_datetime(orders_data['ord_date'])
monthly_purch_amt = orders_data.groupby(orders_data['ord_date'].dt.to_period('M'))['purch_amt'].sum()
print("\nMonth-wise Purchase Amount:")
print(monthly_purch_amt)
# Line chart plotting
monthly_purch_amt.plot(kind='line', title='Month-wise Purchase Amount')
plt.xlabel('Order Date (Month)')
plt.ylabel('Total Purchase Amount')
plt.legend(['purch_amt'])
plt.show()


# Lab4: Write a Pandas program to split the following data frame into groups and calculate monthly purchase amount.Also generate a bar chart based on
# the result and explain the conclusion.
print("\n__________Answer4__________")
df = pd.DataFrame({'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
'ord_date':['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012',
            '04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

print("Original Orders dataframe: \n", df)
stats = df.groupby(['customer_id', 'salesman_id'])['purch_amt'].agg(['mean', 'min', 'max'])
stats.plot(kind='bar', figsize=(12, 6))
plt.title('Mean, Min, and Max Purchase Amount per Customer and Salesman')
plt.xlabel('Customer ID and Salesman ID')
plt.ylabel('Purchase Amount')
plt.legend(title='Statistics')
plt.tight_layout()
plt.show()
