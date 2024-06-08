from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = []

ans = 0

for i in range(n):
    diff.append(a[i] - b[i])

diff.sort()
j = n

for i in range(n):
    while j > 0 and diff[i] + diff[j-1] > 0:
        j -= 1
    ans += n - max(j, i+1)

        
print(ans)