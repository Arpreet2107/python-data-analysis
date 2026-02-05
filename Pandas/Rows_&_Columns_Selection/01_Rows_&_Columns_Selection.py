import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)
# select single column
df[['Name']]

# Name
# 0	Madhav
# 1	Vishakha
# 2	Lalita
# 3	Rishabh

# select multiple columns
df[['Name', 'Monthly_Salary']]

# Name	Monthly_Salary
# 0	Madhav	90000
# 1	Vishakha	70000
# 2	Lalita	50000
# 3	Rishabh	30000

# select single row || loc - label based index
df.loc[df.Name=='Madhav']

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000

# select multiple rows || loc - label based index
df.loc[(df.Name=='Madhav') & (df.Monthly_Salary>=50000)]

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000

df.loc[0:2]

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
# 2	Lalita	18	50000

# Select Rows || iloc - index-value based
# df.iloc[0]
df.iloc[0:2] # [start:stop:step]

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000

