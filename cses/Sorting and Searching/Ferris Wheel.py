n,x = map(int, input().split())
w = list(map(int,input().split()))
w.sort()

count = 0
i = 0
j = n - 1

while i < n - 1 and j > i:
    if w[i] + w[j] <= x:
        count += 1
        w[j] = 100 ** 10
        i += 1
        j = n - 1
    else:
        j -= 1

print(count)
    