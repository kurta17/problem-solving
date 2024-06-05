n,k = map(int, input().split())
a = list(map(int, input().split()))
ans = []

if k % 2 != 0:
    for i in range(n-k+1):
        segm = a[i:i+k]
        segm.sort()
        ans.append(segm[(k)//2])
else:
    for i in range(n-k+1):
        segm = a[i:i+k]
        segm.sort()
        ans.append(min(segm[(k)//2], segm[(k)//2 + 1]))
    
print(*ans)
