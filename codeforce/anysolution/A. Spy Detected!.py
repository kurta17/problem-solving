t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    while k < n- 1:
        if a[k] == a[k+1]:
            k += 1
        else:
            break
    if a[k] == a[k-1]:
        print(k+2)
    else:
        print(k+1)