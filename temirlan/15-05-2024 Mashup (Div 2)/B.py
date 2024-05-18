t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    ans = True
    

    for i in range(n-1):
        if b[i] == 1 and a[i] == 0:
            a[i+1] = 1
        elif b[i] == 1 and a[i] != 0:
            a[i+1] = 0
        else:
            a[i+1] = a[i]
    
    
    if b[n-1] == 1 and a[n-1] != a[0]:
        print("YES")
    elif b[n-1] == 0 and a[n-1] == a[0]:
        print("YES")
    else:
        print("NO")