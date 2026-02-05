import matplotlib.pyplot as plt

# used to show part-to-whole relationships/data\
# data
categories = ['A','B','C','D','E']
sales = [10, 20, 55, 35, 45]

plt.pie(sales, labels=categories, autopct = '%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.show()