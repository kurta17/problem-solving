t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    first = 0
    last = 0

    for i in range(n):
        if a[i] == 1:
            first = i
        elif a[i] == n:
            last = i
    
    if first < last:
        print((first + (n - last - 1)))
    else:    
        print((first + (n - last - 2)))