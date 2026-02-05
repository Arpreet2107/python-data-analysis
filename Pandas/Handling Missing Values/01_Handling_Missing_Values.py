import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)   
# 	Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000	CEO	2024-01-01	1
# 1	Vishakha	17	70000	HR	2024-01-15	1
# 2	Lalita	18	50000	CTO	2024-03-28	3
# 3	Rishabh	19	30000	DA	2024-03-03	3

df.isnull() #  Detect missing values

# Name	Age	Salary	Team	DOJ	Month
# 0	False	False	False	False	False	False
# 1	False	False	False	False	False	False
# 2	False	False	False	False	False	False
# 3	False	False	False	False	False	False

import numpy as np  # to create null values below
df.loc[df.Name=='Rishabh', 'Salary'] = np.nan # adding a null value
print(df)
# 	Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1
# 2	Lalita	18	50000.0	CTO	2024-03-28	3
# 3	Rishabh	19	NaN	DA	2024-03-03	3

df.isnull()

# Name	Age	Salary	Team	DOJ	Month
# 0	False	False	False	False	False	False
# 1	False	False	False	False	False	False
# 2	False	False	False	False	False	False
# 3	False	False	True	False	False	False

df.isnull().sum() # count of null values by columns
# Name      0
# Age       0
# Salary    1
# Team      0
# DOJ       0
# Month     0
# dtype: int64
df.fillna(0) # fill null values with 0
# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1
# 2	Lalita	18	50000.0	CTO	2024-03-28	3
# 3	Rishabh	19	0.0	DA	2024-03-03	3

df.loc[df.Name=='Rishabh', 'Salary'] = 30000
print(df)
# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1
# 2	Lalita	18	50000.0	CTO	2024-03-28	3
# 3	Rishabh	19	30000.0	DA	2024-03-03	3

