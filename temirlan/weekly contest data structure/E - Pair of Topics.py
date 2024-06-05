from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = defaultdict(int)
ans = 0

for i in range(n):
    d = a[i] - b[i]
    
                
print(ans)
        