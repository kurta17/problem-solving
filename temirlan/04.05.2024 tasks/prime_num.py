import math
x = int(input())

k = int(math.sqrt(x))

divis = []

for i in range(1,k):
    if x % i == 0:
        divis.append(x//i)
        divis.append(i)

print(divis)
print(len(divis))