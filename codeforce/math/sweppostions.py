import math
import matplotlib.pyplot as plt
import random
import numpy as np

tot = []

for _ in range(3):
    rand_ver = [random.random() for _ in range(5000)]
    tot.append(rand_ver)

# Calculate the average value of each list in tot
averages = []

for i in range(5000):
    sum = 0
    for k in range(3):
        sum += tot[k][i]
    averages.append(sum / 3)
n = int(math.sqrt(5000) // 3)
print(n)

# plot the averages histogram
plt.hist(averages, bins=n, edgecolor='black',log=True)
plt.title('Histogram of Averages')
plt.xlabel('Average')
plt.ylabel('Frequency')

# Show the plot
plt.show()
 
 

    


