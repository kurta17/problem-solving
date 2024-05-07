import math
x = int(input())

k = int(math.sqrt(x))

sum_divis = 0

for i in range(1,k+1,2):
    if x % i == 0:
        if i == x//i:
            sum_divis += i
        else:
            sum_divis += i
            sum_divis += x//i

print(sum_divis)