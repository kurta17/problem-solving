import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = sum(a)
    sqrt_total = int(math.sqrt(k))
    if sqrt_total**2 == k:
        print("YES")
    else:
        print("NO")