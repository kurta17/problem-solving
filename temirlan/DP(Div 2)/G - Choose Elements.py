n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dpa = [False ]  * (n+1)
dpb = [False ]  * (n+1)
dpa[0] = True
dpb[0] = True

for i in range(1,n):
    if dpa[i-1]:
        if abs(a[i] - a[i-1]) <= k:
            dpa[i] = True
        if abs(b[i] - a[i-1]) <= k:
            dpb[i] = True
    if dpb[i-1]:
        if abs(a[i] - a[i-1]) <= k:
            dpa[i] = True
        if abs(b[i] - b[i-1]) <= k:
            dpb[i] = True

if dpa[n-1] or dpb[n-1]:
    print("YES")
else:
    print("NO")
