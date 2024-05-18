n,k = map(int, input().split())
a = list(map(int, input().split()))

ind = [0] * n
ans = a.sort()

for i in range(n):
    for k in range(k):
        if ans[i] == a[k]:
            ind[i] = k
            break

ans = True

for i in ind:
    for n in range()
    if i - k < 0:
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")
    
    