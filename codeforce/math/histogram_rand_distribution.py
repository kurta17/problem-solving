import random
import matplotlib.pyplot as plt
import math

# Generate 5000 random numbers
numbers = [random.random() for _ in range(5000)]
# sqrt_numbers = [math.sqrt(i) for i in numbers]
# sqrt_numbers.sort()
numbers_abs = [abs(2 * i - 1) for i in numbers]
numbers_abs.sort()
probabilities = [i/5000 for i in range(5000)]

# # Create a histogram of the square roots
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.hist(sqrt_numbers, bins=50, edgecolor='black', density=probabilities)
# plt.title('Histogram of sqrt(Theta)')
# plt.xlabel('sqrt(Theta)')
# plt.ylabel('Probability Density')

# Create a plot of the square roots and their probabilities
probabilities = [i/5000 for i in range(5000)]
plt.subplot(1, 2, 2)
plt.plot(numbers_abs, probabilities)
plt.title('Plot of sqrt(Theta) and Probability')
plt.xlabel('sqrt(Theta)')
plt.ylabel('Probability')

# Show the plots
plt.tight_layout()
plt.show()