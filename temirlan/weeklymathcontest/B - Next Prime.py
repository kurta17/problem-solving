import math

x = int(input())

is_prime = [x > 1 for x in range(2 * x)]
 
for i in range(2, int(math.sqrt(2 * x) + 1)):
	if is_prime[i]:
		for j in range(i * i, 2 * x, i):
			is_prime[j] = False

for i in range(len(is_prime)):
	if i >= x and is_prime[i] == True:
		print(i)
		break