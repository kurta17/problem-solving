n,m = map(int, input().split())
n = list(map(int, input().split()))
m = list(map(int, input().split()))

n.sort()
m.sort()

i = 0
j = 0

ans = float('inf')

while i < len(n) and j < len(m):  
    ans = min(ans, abs(n[i] - m[j]))
    if n[i] < m[j]:
        i += 1
    else:
        j += 1

print(ans)  
