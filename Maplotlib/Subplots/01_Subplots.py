import matplotlib.pyplot as plt

# used to show multiple charts in one figure

# data-1 - bar chart
categories = ['Mon','Tue','Wed','Thu','Fri']
sales = [10, 20, 55, 35, 45]

# data-2 - scatter plot
y1 = [10, 20, 25, 35, 45]
y2 = [20, 30, 35, 45, 55]

plt.figure(figsize=(10,4))

# first plot- bar chart
plt.subplot(1,2,1) # row, column, position
plt.bar(categories, sales)
plt.title("Daily Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")


# second plot- scatter chart
plt.subplot(1,2,2) # row, column, position
plt.scatter(y1, y2)
plt.title("User Example")
plt.xlabel("User1")
plt.ylabel("User2")

plt.show()