# using a List
import pandas as pd
df = pd.DataFrame([11,22,33], columns=['Col_Name'])
print(df)
#    Col_Name
# 0        11
# 1        22
# 2        33
print(type(df)) # check data type
#<class 'pandas.core.frame.DataFrame'>
# using Dictionary of Lists
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)
#        Name  Age  Salary
# 0    Madhav   16   90000
# 1  Vishakha   17   70000
# 2    Lalita   18   50000
# 3   Rishabh   19   30000
print(type(df)) # check data type
#<class 'pandas.core.frame.DataFrame'>