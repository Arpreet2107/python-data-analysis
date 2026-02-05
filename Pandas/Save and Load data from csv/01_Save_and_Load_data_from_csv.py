import pandas as pd
data = {
    'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
    'Age': [16,17,18,19],
    'Salary': [90000, 70000, 50000, 30000]
}
df = pd.DataFrame(data)
print(df)
df.to_csv('Test_data.csv', index=False) # save file - export data frame to csv file
load_df= pd.read_csv('Test_data.csv') # load file - import dataframe
print(load_df)

# Name	Age	Monthly_Salary
# 0	Madhav	16	90000
# 1	Vishakha	17	70000
# 2	Lalita	18	50000
# 3	Rishabh	19	30000

