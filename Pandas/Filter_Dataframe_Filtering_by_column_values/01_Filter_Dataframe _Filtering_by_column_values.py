import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)
# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
# 2	Lalita	18	50000
# 3	Rishabh	19	30000
df_age_filter = df[df['Age'] >= 18] # filter and store dataframe in a new variable
print(df_age_filter)

# Name	Age	Monthly_Salary
# 2	Lalita	18	50000
# 3	Rishabh	19	30000
df_salary_filter = df[df['Monthly_Salary'] >= 50000] # filter and store dataframe in a new variable
print(df_salary_filter) 
# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
# 2	Lalita	18	50000

df[(df['Age'] >= 18) & (df['Monthly_Salary'] >= 50000)] # multiple filter conditions
# Name	Age	Monthly_Salary
# 2	Lalita	18	50000

df.where(df['Age'] >= 18) # where function replace values in a DataFrame based on a condition
# Name	Age	Monthly_Salary
# 0	NaN	NaN	NaN
# 1	NaN	NaN	NaN
# 2	Lalita	18.0	50000.0
# 3	Rishabh	19.0	30000.0
df.where(df['Age'] >= 18, other = 'Not Eligible')
# Name	Age	Monthly_Salary
# 0	Not Eligible	Not Eligible	Not Eligible    
# 1	Not Eligible	Not Eligible	Not Eligible
# 2	Lalita	18.0	50000.0
# 3	Rishabh	19.0	30000.0