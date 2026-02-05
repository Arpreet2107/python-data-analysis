import matplotlib.pyplot as plt
# used for distribution analysis
# data
import random
data = [random.randint(1, 20) for _ in range(500)]

plt.hist(data, bins=20) # histogram chart
plt.title("Histogram Example")
plt.show()
