import math

def sieve(limit):
    divisors = [0] * (limit + 1)  
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            divisors[j] += 1

    return divisors

limit = 10 ** 6
divisors = sieve(limit)
#print(divisors)

n = int(input())

for _ in range(n):
    a = int(input())
    print(divisors[a])
