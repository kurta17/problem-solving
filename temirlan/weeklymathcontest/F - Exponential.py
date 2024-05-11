import math

def max_power_num(x):
    max_power = 1
    
    for b in range(2, int(x ** 0.5) + 1):
        p = 2
        while b ** p <= x:
            max_power = max(max_power, b ** p)
            p += 1
        
    return max_power

n = int(input())
print(max_power_num(n))
