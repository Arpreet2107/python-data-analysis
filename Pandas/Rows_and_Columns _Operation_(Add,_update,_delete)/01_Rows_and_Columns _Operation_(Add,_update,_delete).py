import pandas as pd
data = {    
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Monthly_Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data) 
print(df)

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
# 2	Lalita	18	50000
# 3	Rishabh	19	30000

# Create a new column
df['Team'] = ['CEO', 'HR', 'CTO', 'DA']
print(df)

# Name	Age	Monthly_Salary	Team
# 0	Madhav	16	90000	CEO
# 1	Vishakha	17	70000	HR
# 2	Lalita	18	50000	CTO
# 3	Rishabh	19	30000	DA
# Add new columns using existing column/s
df['Bonus'] = df['Monthly_Salary'] * 0.20
print(df)
# Name	Age	Monthly_Salary	Team	Bonus
# 0	Madhav	16	90000	CEO	18000.0
# 1	Vishakha	17	70000	HR	14000.0
# 2	Lalita	18	50000	CTO	10000.0
# 3	Rishabh	19	30000	DA	6000.0
# Add new row - at the end of dataframe
df.loc[len(df)] = ['ABC', 21, 21000, 'IT', 2000]
print(df)
# Name	Age	Monthly_Salary	Team	Bonus
# 0	Madhav	16	90000	CEO	18000.0
# 1	Vishakha	17	70000	HR	14000.0
# 2	Lalita	18	50000	CTO	10000.0
# 3	Rishabh	19	30000	DA	6000.0
# update value in dataframe using index-name
df.loc[0, 'Monthly_Salary'] = 95000
print(df)
# Name	Age	Monthly_Salary	Team	Bonus
# 0	Madhav	16	95000	CEO	18000.0
# 1	Vishakha	17	70000	HR	14000.0
# 2	Lalita	18	50000	CTO	10000.0
# 3	Rishabh	19	30000	DA	6000.0

# update value in dataframe using column-value
df.loc[df.Name=='Madhav','Monthly_Salary'] = 90000
print(df)
# Name	Age	Monthly_Salary	Team	Bonus
# 0	Madhav	16	90000	CEO	18000.0
# 1	Vishakha	17	70000	HR	14000.0
# 2	Lalita	18	50000	CTO	10000.0
# 3	Rishabh	19	30000	DA	6000.0  
# delete value - rows and columns
df.drop('Bonus', axis=1, inplace=True) # delete column
print(df)   
# Name	Age	Monthly_Salary	Team    
# 0	Madhav	16	90000	CEO 
# 1	Vishakha	17	70000	HR
# 2	Lalita	18	50000	CTO
# 3	Rishabh	19	30000	DA
# delete row using column-value filter
df = df.drop(df[df.Name == 'ABC'].index) # delete row, axis= 0
print(df)
# Name	Age	Monthly_Salary	Team
# 0	Madhav	16	90000	CEO
# 1	Vishakha	17	70000	HR
# 2	Lalita	18	50000	CTO
# 3	Rishabh	19	30000	DA
# delete row using index-name filter
df.drop(1, axis=0)
# Name	Age	Monthly_Salary	Team
# 0	Madhav	16	90000	CEO
# 2	Lalita	18	50000	CTO
# delete row using index-name filter and inplace = True 
df.drop(1, axis=0, inplace=True)
print(df)
# Name	Age	Monthly_Salary	Team
# 0	Madhav	16	90000	CEO
# 2	Lalita	18	50000	CTO                     
df.drop('Bonus', axis=1, inplace=True) # delete one column
# df.drop(['Bonus', 'Team'], axis=1, inplace=True) # delete multiple columns
df.rename(columns={'Monthly_Salary': 'Salary'}, inplace=True) # rename column name
print(df)
# Name	Age	Salary	Team
# 0	Madhav	16	90000	CEO 
# 2	Lalita	18	50000	CTO


# sort values - order values in dataframe by asc or desc order
df.sort_values('Salary') #ascending order, by default
# Name	Age	Salary	Team    
# 2	Lalita	18	50000	CTO 
# 0	Madhav	16	90000	CEO
df.sort_values('Salary', ascending=False) # descending order    
# Name	Age	Salary	Team    
# 0	Madhav	16	90000	CEO
# 2	Lalita	18	50000	CTO         

                                        

                                                                