# Lab1: Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
import pandas as pd
import numpy as np

df = pd.read_csv('salesdata.csv')

table = pd.pivot_table(df, index=['Region', 'Manager', 'SalesMan'], values=['Sale_amt'], aggfunc=np.sum, fill_value=0)
print(table)

# Lab2: Write a Pandas program to create a Pivot table and find the item wise unit sold.
import pandas as pd
import numpy as np

df = pd.read_csv('salesdata.csv')

table = pd.pivot_table(df, index=['Item'], values=['Units'], aggfunc=np.sum, fill_value=0)
print(table)

# Lab3: Write a Pandas program to create a Pivot table and find the region wise, item wise unit sold.
import pandas as pd
import numpy as np

df = pd.read_csv('salesdata.csv')

table = pd.pivot_table(df, index=['Region', 'Item'], values=['Units'], aggfunc=np.sum, fill_value=0)
print(table)

# Lab4: Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount.
import pandas as pd
import numpy as np

df = pd.read_csv('salesdata.csv')

table = pd.pivot_table(df, index=['Manager'], values=['Sale_amt'], aggfunc={'Sale_amt':[len, np.mean]}, fill_value=0)
print(table)

