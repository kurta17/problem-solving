m,n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
count = 0
inf = 10**10
j = 0

for i in range(m):
    while j < n:
        if a[i] - k <= b[j]:
            break
        else:
            j += 1

    if j < n and a[i] - k <= b[j] <= a[i] + k:
        count += 1
        j += 1

print(count)
