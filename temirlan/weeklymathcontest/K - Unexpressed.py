import math
n = int(input())
ans = set()
count = 0
for a in range(2, int(math.sqrt(n)) + 1):
    for b in range(2, int(math.log(n, a)) + 1):
        if a**b <= n:
            ans.add(a**b)

print(n - len(ans))
