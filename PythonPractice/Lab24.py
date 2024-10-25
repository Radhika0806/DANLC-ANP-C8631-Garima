import numpy as np
import pandas as pd

# Lab1: Write a Pandas program to detect missing values of a given DataFrame.
print("__________Answer1__________")
df1 = pd.DataFrame({'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10',
                                '2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
                   'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("\nOriginal Orders DataFrame:\n", df1)
print("\nMissing values of the said dataframe:\n")

null_val = df1.isnull().sum()
print(null_val)

# Lab2: Write a Pandas program to drop the rows where at least one element is missing in a given DataFrame
print("\n__________Answer2__________")
df2 = pd.DataFrame({'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10'
                                    ,'2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
                   'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})

print("\nOriginal Orders DataFrame:\n", df2)
print("\nDrop the rows where at least one element is missing")
print(df2.dropna())

# Lab3: Write a Pandas program to drop the rows where all elements are missing in a given DataFrame
print("\n__________Answer3__________")
df3 = pd.DataFrame({'ord_no':[np.nan,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[np.nan,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date':[np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10',
                               '2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[np.nan,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001]})

print("\nOriginal Orders DataFrame:\n",df3)
print("\nDrop the rowswhere all elements are missing:")
print(df3.dropna(how='all'))

# Lab4: Write a Pandas program to drop those rows from a given DataFrame in which specific columns have missing values
print("\n__________Answer4__________")
df4 = pd.DataFrame({'ord_no':[np.nan,np.nan,70002,np.nan,np.nan,70005,np.nan,70010,70003,70012,np.nan,np.nan],
                   'purch_amt':[np.nan,270.65,65.26,np.nan,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,np.nan],
                   'ord_date':[np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10',
                               '2012-06-27','2012-08-17',np.nan],
                   'customer_id':[np.nan,3001,3001,np.nan,3002,3001,3001,3004,3003,3002,3001,np.nan]})

print("\nOriginal Orders DataFrame:\n", df4)
print("\nDrop those rows in which specific columns have missing values: ")
print(df4.dropna(subset=['ord_no', 'purch_amt', 'customer_id']))













