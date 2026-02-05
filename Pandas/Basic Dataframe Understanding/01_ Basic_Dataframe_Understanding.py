import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)
df.head(2) # top rows
# 	Name	Age	Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
df.tail(2) # last rows

# Name	Age	Salary
# 2	Lalita	18	50000
# 3	Rishabh	19	30000

df.shape # returns a tuple containing the shape of the DataFrame - rows & columns
#(4, 3)
df.columns # list of column names in a dataframe
#Index(['Name', 'Age', 'Salary'], dtype='object')
df.dtypes # data types of each column
df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True) # rename column name/s
print(df)
#        Name  Age  Monthly_Salary  
# 0    Madhav   16           90000
# 1  Vishakha   17           70000
# 2    Lalita   18           50000
# 3   Rishabh   19           30000
df.info()  # info method prints information about the DataFrame
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column          Non-Null Count  Dtype 
# ---  ------          --------------  ----- 
#  0   Name            4 non-null      object
#  1   Age             4 non-null      int64 
#  2   Monthly_Salary  4 non-null      int64 
# dtypes: int64(2), object(1)
# memory usage: 228.0+ bytes
df.describe() # describe method generates descriptive statistics of DataFrame, only for numerical-value columns

#       Age	        Monthly_Salary
# count	4.000000	4.000000
# mean	17.500000	60000.000000
# std	1.290994	25819.888975
# min	16.000000	30000.000000
# 25%	16.750000	45000.000000
# 50%	17.500000	60000.000000
# 75%	18.250000	75000.000000
# max	19.000000	90000.000000
