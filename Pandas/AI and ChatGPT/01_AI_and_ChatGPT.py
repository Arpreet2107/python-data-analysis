import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita ', 'Rishabh'],
    'Age': [16, 17, 18, 19],
    'Salary': [90000.0, 70000.0, 50000.0, 30000.0],
    'Team': ['CEO', 'HR', 'CTO', 'DA'],
    'DOJ': ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03']
}
df = pd.DataFrame(data)
df['DOJ'] = pd.to_datetime(df['DOJ'])
df['Month'] = df['DOJ'].dt.month
print(df)   
    
# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1
# 2	Lalita	18	50000.0	CTO	2024-03-28	3
# 3	Rishabh	19	30000.0	DA	2024-03-03	3

# Prompt to filter salary > 70000 and January employees
# Method-1: basic filter
df[(df['Month'] == 1) & (df['Salary'] >= 70000)]

# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1

# Method-2: using query method
df.query('Month == 1 and Salary >= 70000')
# Name	Age	Salary	Team	DOJ	Month
# 0	Madhav	16	90000.0	CEO	2024-01-01	1
# 1	Vishakha	17	70000.0	HR	2024-01-15	1



