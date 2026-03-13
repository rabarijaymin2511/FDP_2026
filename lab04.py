import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [1000, 1500, 1200, 1800, 2000]


plt.plot(days, sales)



plt.title("Weekly Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales Amount")


plt.show()

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
