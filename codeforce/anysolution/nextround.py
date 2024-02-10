n,k = map(int, input().split())
mlist = list(map(int, input().split()))
count = 0
kthplace = mlist[k - 1]
for i in range(n):
    if mlist[i] != 0 and mlist[i] >= kthplace:
        count += 1
print(count)
