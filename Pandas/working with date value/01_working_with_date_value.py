import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)   
# create a date column - date of joining
df['DOJ'] = ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03']
print(df)
# Name	Age	Salary	DOJ
# 0	Madhav	16	90000	2024-01-01
# 1	Vishakha	17	70000	2024-01-15
# 2	Lalita	18	50000	2024-03-28
# convert date column to datetime format
df['DOJ'] = pd.to_datetime(df['DOJ'])
print(df)   
# Name	Age	Salary	DOJ 
# 0	Madhav	16	90000	2024-01-01  
# 1	Vishakha	17	70000	2024-01-15      

df['DOJ'].dtype # object-type value
# datetime64[ns] - datetime format value    

df['DOJ'] = pd.to_datetime(df['DOJ']) # change to date-time type
print(df['DOJ'].dtype) # check data type
# datetime64[ns] - datetime format value

# creating a new column with incorrect date format
df1['DOJ2'] = ['01-01-2025', '15-01-2025', '28-03-2025', '03-03-2025']
print(df1)
# Name	Age	Salary	DOJ2    
# 0	Madhav	16	90000	01-01-2025  
# 1	Vishakha	17	70000	15-01-2025
# 2	Lalita	18	50000	28-03-2025
df1['DOJ2'].dtype  # object-type value
df1['DOJ2'] = pd.to_datetime(df1['DOJ2'], format = '%d-%m-%Y') # change to date-time type using date-format
print(df1['DOJ2'].dtype) # check data type
# datetime64[ns] - datetime format value
df = df.drop('DOJ2', axis=1)
# extract year, month, week, day
df['DOJ'].dt.year
df['DOJ'].dt.month
df['DOJ'].dt.day
df['DOJ'].dt.day_name()

# create new column using month extract function from DOJ column
df['Month'] = df['DOJ'].dt.month
# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000	CEO	2024-01-01	1
# 1	Vishakha	17	70000	HR	2024-01-15	1
# 2	Lalita	18	50000	CTO	2024-03-28	3
# 3	Rishabh	19	30000	DA	2024-03-03	3


[df'DOJ'] + pd.Timedelta(days=90) # add 90 days to DOJ column
# 0   2024-03-31
# 1   2024-04-14
# 2   2024-06-26
# 3   2024-06-01
# Name: DOJ, dtype: datetime64[ns]
