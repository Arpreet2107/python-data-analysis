import  matplotlib.pyplot as plt
# data
x = [1,2,3,4,5]
y1 = [10, 20, 25, 35, 45]
y2 = [20, 30, 35, 45, 55]

plt.plot(x, y1, label='Sales 2024') # ploting y1 data
plt.plot(x, y2, label='Sales 2025') # ploting y2 data

plt.title("YoY Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend() # show legends
plt.show()
