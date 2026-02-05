import matplotlib.pyplot as plt


plt.figure(figsize=(4,3)) # figure size

plt.plot(x, y, color='blue', marker='o', linestyle='--', linewidth=2, markersize=12)

plt.title("Kuch bhi Title hai")
plt.xlabel("x-axis label hai")
plt.ylabel("y-axis label hai")

plt.show()
