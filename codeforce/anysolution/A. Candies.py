import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    k_sum = 3
    i = 2
    while n % k_sum != 0:
        k_sum += 2**i
        i += 1
    res = n // k_sum
    print(res)

    

