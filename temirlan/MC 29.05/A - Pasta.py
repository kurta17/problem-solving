

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = dict()

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

for i in range(m):
    if b[i] in d:
        d[b[i]] -= 1
        if d[b[i]] < 0:
            print("NO")
            exit()
    else:
        print("NO")
        exit()
else:
    print("YES")

