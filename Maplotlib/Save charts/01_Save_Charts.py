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
                                                 

plt.bar(df['Month'], df['Sales'])
plt.title("Matplotlib with Pandas")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("Monthly_Sales_from_df.png")

plt.show()

