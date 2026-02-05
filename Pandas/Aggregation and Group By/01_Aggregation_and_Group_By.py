import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000],
    'Team': ['CEO', 'HR', 'CTO', 'DA'],
    'DOJ': ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03'],
    'Month': [1, 1, 3, 3]
}
df = pd.DataFrame(data)
print(df)
df['Month'].value_counts() # frequency of values in month column
# Month
# 1    2
# 3    2
# Name: count, dtype: int64
df[df['Month']==1].value_counts() # frequency of values in month column where month=1
# Name      Age  Salary   Team  DOJ         Month
# Madhav    16   90000.0  CEO   2024-01-01  1        1
# Vishakha  17   70000.0  HR    2024-01-15  1        1
# Name: count, dtype: int64
# aggregation based on group by
df.groupby('Month')['Salary'].sum() # sum of salary by month
# Month
# 1    160000.0
# 3     80000.0
# Name: Salary, dtype: float64
# different aggregation on different columns
df.groupby('Month').agg({'Salary': 'mean', 'Name': 'count'})
# 	Salary	Name
# Month		
# 1	80000.0	2
# 3	40000.0	2
