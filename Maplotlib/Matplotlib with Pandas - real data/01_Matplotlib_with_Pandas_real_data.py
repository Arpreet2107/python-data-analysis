import matplotlib.pyplot as plt
# create df
from calendar import Month
import pandas as pd

# data
data = {
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales' : [12000, 11000, 13000, 25000]
}

df = pd.DataFrame(data)
print(df)

# Month	Sales
# 0	Jan	12000
# 1	Feb	11000
# 2	Mar	13000
# 3	Apr	25000


plt.bar(df['Month'], df['Sales'])
plt.title("Matplotlib with Pandas")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

