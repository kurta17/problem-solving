from collections import defaultdict

n,q = map(int, input().split()) 
a = list(map(int, input().split()))

freq = [0] * (n+1)  
query = []

for i in range(q):
    l,r = map(int, input().split())
    query.append((l,r))
    freq[l-1] += 1
    if r < n:
        freq[r] -= 1

for i in range(1,n):
    freq[i] += freq[i-1]

freq = freq[:-1]
a.sort(reverse=True)
freq.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * freq[i]

print(ans)
