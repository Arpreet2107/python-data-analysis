import pandas as pd 
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data) 
print(df)

df1 = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
print(df1)

# ID	Name
# 0	1	A
# 1	2	B
# 2	3	C
df2 = pd.DataFrame({'ID':[1,2,2,4],'Score':[88,96,77,79]})
print(df2)

# ID	Score
# 0	1	88
# 1	2	96
# 2	2	77
# 3	4	79
# Concatenate: vertical / row level / top on top
pd.concat([df1, df2], axis=0)

# ID	Name	Score
# 0	1	A	NaN
# 1	2	B	NaN
# 2	3	C	NaN
# 0	1	NaN	88.0
# 1	2	NaN	96.0
# 2	2	NaN	77.0
# 3	4	NaN	79.0
# Concatenate: horizontal / column level / side by side
pd.concat([df1, df2], axis=1)
# ID	Name	ID	Score
# 0	1	A	1	88
# 1	2	B	2	96  
# 2	3	C	2	77
# 3	NaN	NaN	4	79
# Merge in Pandas
# Performs join operations similar to
# Merge: based on common column - ID
pd.merge(df1, df2, on='ID', how='inner') # inner join
# ID	Name	Score               
# 0	1	A	88  
# 1	2	B	96
# 2	2	B	77

pd.merge(df1, df2, on='ID', how='left') # left join
# ID	Name	Score   
# 0	1	A	88.0    
# 1	2	B	96.0        
# 2	2	B	77.0    
# 3	C	NaN 
