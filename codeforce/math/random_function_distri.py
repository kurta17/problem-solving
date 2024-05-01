import random
import matplotlib.pyplot as plt
import math

# Generate 5000 random numbers
numbers = [random.random() for _ in range(5000)]
# sqrt_numbers = [math.sqrt(i) for i in numbers]
# sqrt_numbers.sort()
numbers_abs = [abs(2 * i - 1) for i in numbers]

probabilities = [i/5000 for i in range(5000)]



# Create a plot of the square roots and their probabilities
plt.plot(numbers_abs, probabilities)

# Set the title and labels
plt.title('Plot of sqrt(Theta) and Probability')
plt.xlabel('sqrt(Theta)')
plt.ylabel('Probability')

# Show the plot
plt.show()
